from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from shield_core import interface
from shield_core.languages import registry as language_registry
from shield_core.models import registry as model_registry

MAX_SNIPPET_BYTES = 200 * 1024
FAMILY_MAP_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "training" / "cwe_family_map.json"
)


def _load_family_map() -> tuple[dict[str, str], str]:
    data = json.loads(FAMILY_MAP_PATH.read_text(encoding="utf-8"))
    return data["cwe_to_family"], data.get("fallback_family", "other")


CWE_TO_FAMILY, FALLBACK_FAMILY = _load_family_map()

app = FastAPI(
    title="SHIELD API",
    version=interface.INTERFACE_VERSION,
    description="HTTP API backed by shield_core.interface",
)


class ScanRequest(BaseModel):
    code: str
    language: str


def _error(status_code: int, code: str, message: str) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={"error": {"code": code, "message": message}},
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(_request: Request, exc: RequestValidationError) -> JSONResponse:
    details = "; ".join(
        f"{'.'.join(str(part) for part in error['loc'][1:]) or 'request'}: {error['msg']}"
        for error in exc.errors()
    )
    return _error(400, "bad_request", details or "Invalid request body")


@app.exception_handler(interface.UnsupportedLanguageError)
async def unsupported_language_handler(
    _request: Request, exc: interface.UnsupportedLanguageError
) -> JSONResponse:
    return _error(422, "unsupported_language", str(exc))


@app.exception_handler(interface.ModelUnavailableError)
async def model_unavailable_handler(
    _request: Request, exc: interface.ModelUnavailableError
) -> JSONResponse:
    return _error(503, "model_unavailable", str(exc))


@app.exception_handler(Exception)
async def unexpected_error_handler(_request: Request, _exc: Exception) -> JSONResponse:
    return _error(500, "internal_error", "The scan could not be completed")


@app.get("/v1/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "schema_version": interface.SCHEMA_VERSION,
        "interface_version": interface.INTERFACE_VERSION,
    }


@app.get("/v1/languages")
def languages() -> dict[str, list[dict[str, Any]]]:
    enabled = [spec for spec in language_registry.all_languages() if spec.enabled]
    return {
        "languages": [
            {"id": spec.name, "extensions": list(spec.extensions), "cwe_list": list(spec.cwes)}
            for spec in enabled
        ]
    }


@app.get("/v1/model")
@app.get("/v1/models", include_in_schema=False)
def model_info() -> dict[str, Any]:
    config = model_registry.default_registry().config
    return {
        "default": config.default,
        "fallback": config.fallback,
        "available": [
            {"version": entry.version, "languages": list(entry.languages)}
            for entry in config.models.values()
        ],
    }


@app.post("/v1/scan")
@app.post("/v1/scan/snippet", include_in_schema=False)
def scan(request: ScanRequest) -> dict[str, Any] | JSONResponse:
    if len(request.code.encode("utf-8")) > MAX_SNIPPET_BYTES:
        return _error(
            413,
            "payload_too_large",
            f"Code exceeds the {MAX_SNIPPET_BYTES // 1024} KB snippet limit.",
        )

    result = interface.predict(request.code, request.language)
    payload = result.to_dict()
    payload["cwe_family"] = (
        CWE_TO_FAMILY.get(result.cwe, FALLBACK_FAMILY) if result.cwe is not None else None
    )
    return payload
