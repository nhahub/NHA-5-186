# SHIELD Adjusted Delivery Plan

> Companion plan for [`SHIELD_PLAN.md`](../../SHIELD_PLAN.md). The master plan stays the long-term record. This file is the short, deadline-driven route and its scope cuts. It assumes the team is finishing Week 2 now.

**Goal:** ship a working, deployed SHIELD app with the current V1 model, tracked experiments, and one measured GNN (V2) attempt. Build only what the demo needs. Do not say the GNN is better unless the frozen evaluation shows it.

**Stack:** Streamlit (UI), FastAPI (API), Docker Compose, the existing `shield_core.interface`, and the existing MLflow helper (D17).

Out of scope unless time is left: Celery, Redis, PostgreSQL, login, repo scanning, VS Code extension, CodeT5, multi-language UI polish.

## 1. Working assumptions

- Week 2 ends with: V1 loading through `shield_core.interface` and the CLI, split QA green, and the graph subset/cache written down. If something is late, the app still uses the best V1 that loads, and the demo says what is not final.
- The UI is a thin client. Streamlit calls FastAPI, and FastAPI calls `shield_core.interface`. No second prediction code anywhere.
- First user flow: paste code → choose language → scan → see vulnerable/clean, **CWE family**, exact CWE (small), confidence, model version. Show a clear error message when something fails.
- Deploy one Docker Compose stack (API + Streamlit) to one Linux VM or container host. One public URL. No database.
- "MLOps" here means: reproducible runs, model version you can trace, an evaluation report, and a repeatable container build/deploy. Not a registry service or auto-retraining.

## 2. Order of work: app first, GNN second

### Finish Week 2 (now)

1. Finish split QA and freeze the leakage-safe manifest.
2. V1 loads through `interface.predict()` and the CLI with the real artifact and version.
3. Per-CWE **and** per-family metrics are saved (already done in W2-P3-03: `docs/modeling/v1_per_cwe.md`, `docs/modeling/v1_per_family.md`). Re-run them on the final V1 once split QA is green. Do not show provisional numbers as final.
4. Write down the graph subset, cache location, extraction failures, and node-embedding status.
5. Drop on purpose: broad V2 features (W2-P3-02), LLM baseline, full-dataset graph extraction.

### Phase A: build and deploy the V1 app (3 days)

| Day | Work | Done when |
|---|---|---|
| 1 | **API + pages with mock data.** P4 builds FastAPI routes (`/v1/health`, `/v1/languages`, `/v1/scan`, `/v1/model`) over `shield_core.interface`. P5 builds the Streamlit shell. Everyone builds their page with fake data. | Health and languages routes work. Every page opens with mock data. |
| 2 | **Connect for real.** Pages call the API instead of mock data. Handle errors, input size and time limits. Scan clean and vulnerable examples. | A local scan uses the real V1 and shows family, CWE, confidence, version. |
| 3 | **Package and deploy.** Docker images for API and Streamlit, Docker Compose, deploy, smoke test, write deploy and rollback steps. | Public (or staging) URL answers health and a scan. |

**Gate:** start the GNN sprint only when the app can scan a snippet with V1, show the result and model version, and recover from errors. If deployment is blocked by infrastructure, a clean local Compose demo is enough for now; keep fixing deployment in parallel.

### Phase B: GNN V2

The app keeps using V1 until the GNN passes the gate in Section 4.

| Day | Work | Done when |
|---|---|---|
| 1 | **Check graph data.** PyG graphs match the frozen train/val/test manifest; label coverage; dropped-graph counts; no split crossing. Cache node embeddings for the subset. | Graph dataset report + subset manifest saved. |
| 2 | **Model A (control).** Small graph-only GNN, fixed seed. | Reproducible run logged. |
| 3 | **Model B (V2).** GNN with CodeBERT node embeddings, same data and labels. No architecture search. | Checkpoint and run info saved. |
| 4 | **Compare.** A, B, V1 and the length-only baseline on the same data. Pick on validation only. Run the frozen test once. | Comparison table (family + CWE). |
| 5 | **Decide.** Write the model card. If V2 passes the gate, add it as an optional model and test it in the app. If not, V1 stays the main model. | Model card + recorded decision; app still works on V1. |

### Week 4 (only if there is time): make it reliable, do not add features

Better errors, input limits, health checks, evaluation report, one-click demo. Repo scanning only if the interface already supports it safely.

## 3. Who owns what

Each person owns **one Streamlit page** and **the backend piece behind it**, plus their model/data work. Build the page with mock data first, then connect it to the API.

App layout (Streamlit multipage):

```
app/
  Home.py              # P5: scan form (paste code, choose language, scan button)
  pages/
    1_Result.py        # P4: verdict, family, CWE, confidence, fix status
    2_Findings.py      # P2: findings list, line numbers, taint path if present
    3_History.py       # P1: scans from this browser session
    4_Model.py         # P3: model version + family and CWE metric tables
api/
  main.py              # P4: FastAPI app
```

| Person | Streamlit page | Backend / model work | Hands off |
|---|---|---|---|
| **P1 — Hatem** | `3_History.py`: scans from this session (`st.session_state`, no database). | Input checks, `/v1/languages`, request size/time limits, checks that the API matches `interface.predict()`. Owns data and split provenance. | Frozen data/split info and API request examples → P5. |
| **P2 — Eyad** | `2_Findings.py`: findings with family, CWE, confidence, file/line if available; taint path only when present. | GNN inference behind the interface; checkpoint loading; fall back to V1 if the GNN fails. | A/B checkpoints and how to load them → P3, P4. |
| **P3 — Atef** | `4_Model.py`: model version, **family table first**, CWE table below it in an expander with a short note on why CWE scores are lower. Reads the saved reports (`v1_per_family.md` / `v1_per_cwe.md` or `metrics.json`). | One command for training/evaluation, MLflow logging, calibration, metrics, length-only baseline (W2-P3-05), and the V1-vs-GNN comparison. | Chosen model + exact run config → P4. Model card → team. |
| **P4 — Bigad** | `1_Result.py`: main result. **Family large**, exact CWE small ("Most likely CWE: CWE-787"), confidence, model version. Never says "verified" without real evidence. | FastAPI app, JSON output, error mapping, `/v1/health`, `/v1/model`, CWE → family mapping in the API, model selection and V1 fallback. | API docs (OpenAPI) → P5. |
| **P5 — Maram** | `Home.py`: app shell, scan form, language choice, API client used by all pages. | Docker/Compose, environment config, CI image build, deployment, smoke test. | Public URL, env vars, rollback steps → team. |

**Rules:**

- P4 owns API integration. P5 owns UI integration and deployment.
- P2 and P3 own model artifacts and evaluation. P1 and P2 approve data/graph validity.
- Nobody changes the interface silently. Write a short change note for any new field.
- **Contract change note (this version):** the API scan response adds `cwe_family` next to `cwe`. It is computed in the API from `cwe_family_map.json` (P4). `shield_core.interface.Result` is not changed.

## 4. GNN V2: one focused experiment

The target is a better model, but it is not guaranteed. If V2 fails the gate, ship V1.

1. **Same data.** V1 and the GNNs use the same leakage-safe train/val/test groups, labels and eligible rows. Select on validation; look at the frozen test once.
2. **Two models only.** A: graph-only control (node-type embeddings). B/V2: frozen CodeBERT node-text embeddings + node/edge-type embeddings + one small GAT or gated GNN + pooling + binary and CWE heads.
3. **Keep it small.** Use only graphs already extracted; node cap per language (Python 750, C/C++ the documented cap); skip and log bad graphs; use the node-embedding cache. Start with Python if C/C++ graphs are not ready.
4. **Check for shortcuts.** Report the length-only baseline and V1 next to the GNN. Report dropped-graph rates and class coverage. No synthetic samples in val/test.
5. **Acceptance gate.** Promote V2 only if it beats V1 on **family macro-F1** on the same validation data, and does not clearly hurt recall on the important families. Confirm once on the frozen test. Exact-CWE scores are reported next to it for information, not used for the decision.

Minimum artifacts: checkpoint, config, fixed seed, dataset/split hash, graph converter/schema version, node-embedding cache info, MLflow run (or saved run JSON), **family and CWE** evaluation tables, short model card.

## 5. MLOps and deployment checklist

- **Track:** use `shield_core/tracking.py` and the MLflow logging already in `scripts/training/v1_pipeline.py`. Log seed, config, dataset/split hashes, graph converter version, metrics, artifact path. Never log source code.
- **Package:** versioned model artifacts; check cold start and V1 fallback. Do not commit large files.
- **Build:** pinned Python packages; one image for FastAPI, one for Streamlit; Compose health checks.
- **Deploy:** deploy the same images you tested locally; secrets stay out of the repo; open only the needed ports; record build tag and date.
- **Operate:** `/v1/health`, request size/time limits, logs without code contents, one smoke scan, rollback to the previous image/model tag.
- **Reproduce:** one command to train/evaluate, one command to start the app. The same model version shows in the API result and in MLflow.

## 6. Demo scope

**Must show:** Streamlit app, language choice, pasted code, V1 result with **family + CWE**, confidence and model version, model page with family and CWE tables, API health, deployed URL. After Phase B: the GNN run record and the comparison with V1.

**Only if already working:** graph/taint evidence in findings, session scan history.

**Not now:** repo/ZIP scanning, job queue, login, PostgreSQL, Redis/Celery, VS Code extension, automatic fixes in the UI, CodeT5, Java, full-dataset graph extraction, augmentation, hyperparameter search, analytics dashboard.

## 7. Definition of done

- A clean checkout builds and starts the app with the documented steps.
- The deployed app scans a snippet and shows the real model's result: family, CWE, confidence, version.
- The API reports health, supported languages, model/schema version and clear errors.
- V1 still loads as fallback.
- The GNN has a reproducible run and a fair comparison with V1 (family and CWE), written down even if it loses.
- No tuning on the test set, no claim for unsupported languages, no "verified" claim without evidence.
