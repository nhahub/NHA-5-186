from fastapi.testclient import TestClient

from api import main
from shield_core.interface import ModelUnavailableError, Result, UnsupportedLanguageError

client = TestClient(main.app)


def test_health_reports_api_and_interface_versions():
    response = client.get("/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "schema_version": "1.0",
        "interface_version": "1.0",
    }


def test_languages_only_lists_enabled_registry_languages():
    response = client.get("/v1/languages")

    assert response.status_code == 200
    ids = {language["id"] for language in response.json()["languages"]}
    assert ids == {"cpp", "python"}


def test_model_endpoint_reports_configured_default_and_fallback():
    response = client.get("/v1/model")

    assert response.status_code == 200
    assert response.json()["default"] == "v1"
    assert response.json()["fallback"] == "stub-v0"


def test_scan_uses_interface_and_adds_cwe_family(monkeypatch):
    called = {}

    def fake_predict(code, language):
        called.update(code=code, language=language)
        return Result(vulnerable=True, cwe="CWE-89", confidence=0.91, model_version="v1")

    monkeypatch.setattr(main.interface, "predict", fake_predict)
    response = client.post("/v1/scan", json={"code": "cursor.execute(query)", "language": "python"})

    assert response.status_code == 200
    assert called == {"code": "cursor.execute(query)", "language": "python"}
    assert response.json()["vulnerable"] is True
    assert response.json()["cwe"] == "CWE-89"
    assert response.json()["cwe_family"] == "input_injection"
    assert response.json()["confidence"] == 0.91
    assert response.json()["model_version"] == "v1"


def test_clean_scan_has_null_cwe_family(monkeypatch):
    monkeypatch.setattr(
        main.interface,
        "predict",
        lambda _code, _language: Result(vulnerable=False, cwe=None, confidence=0.8),
    )

    response = client.post("/v1/scan", json={"code": "print('hello')", "language": "python"})

    assert response.status_code == 200
    assert response.json()["cwe"] is None
    assert response.json()["cwe_family"] is None


def test_scan_returns_standard_error_for_unsupported_language(monkeypatch):
    def reject_language(_code, _language):
        raise UnsupportedLanguageError("Unsupported language: cobol")

    monkeypatch.setattr(main.interface, "predict", reject_language)
    response = client.post("/v1/scan", json={"code": "x", "language": "cobol"})

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "unsupported_language"


def test_scan_returns_standard_error_when_model_is_unavailable(monkeypatch):
    def unavailable(_code, _language):
        raise ModelUnavailableError("model unavailable")

    monkeypatch.setattr(main.interface, "predict", unavailable)
    response = client.post("/v1/scan", json={"code": "x", "language": "python"})

    assert response.status_code == 503
    assert response.json()["error"]["code"] == "model_unavailable"


def test_missing_scan_fields_return_bad_request():
    response = client.post("/v1/scan", json={"code": "x"})

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "bad_request"


def test_oversized_scan_is_rejected_before_prediction(monkeypatch):
    def should_not_predict(_code, _language):
        raise AssertionError("prediction should not run for oversized snippets")

    monkeypatch.setattr(main.interface, "predict", should_not_predict)
    response = client.post(
        "/v1/scan",
        json={"code": "x" * (main.MAX_SNIPPET_BYTES + 1), "language": "python"},
    )

    assert response.status_code == 413
    assert response.json()["error"]["code"] == "payload_too_large"
