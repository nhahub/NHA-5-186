# SHIELD Adjusted Delivery Plan

> Companion execution plan for the existing [`SHIELD_PLAN.md`](../../SHIELD_PLAN.md). The master plan remains the long-term record; this document records the deadline-driven MVP route and its scope cuts. It assumes the team is finishing Week 2 now.

**Goal:** deliver a working, deployable SHIELD application with the current V1 model, experiment tracking, and a measured GNN V2 improvement attempt. Build only the user-facing path needed to demonstrate the product. Do not claim the GNN is better unless the frozen evaluation supports it.

**Stack:** React, FastAPI, Docker Compose, existing `shield_core.interface`, existing MLflow tracking helper (D17). This is an adjusted-plan choice; the master plan's Angular decision remains unchanged. Keep the app synchronous for pasted-code scans; defer Celery, Redis, PostgreSQL, auth, repo ingestion, VS Code, CodeT5, and multi-language UI polish unless the deadline has room.

## 1. Working assumptions and project boundary

- Week 2 ends with the real V1 wired through `shield_core.interface` and CLI, split QA green, and the chosen graph subset/cache documented. If one is late, the product must still serve the best loadable V1 artifact; mark model quality and data limits in the demo.
- The app is a thin client of the frozen Python interface/API contract. Do not create a second prediction implementation in the API.
- First usable flow: paste a supported code snippet → select language → scan → view vulnerable/clean, CWE, confidence, model version, and findings. Include a clear unavailable/error state.
- Deploy one Docker Compose stack to a single Linux VM or an available managed container host. For the deadline demo, use one public URL, one API process, and one React build. Persistent job/database services are out of scope.
- “MLOps” for this delivery means reproducible runs, model/version traceability, evaluation artifact, and a repeatable container build/deploy. It does not mean a full model registry service or continuous retraining platform.

## 2. Delivery sequence: application first, GNN second

### Finish Week 2 (now): stabilize the model seam

Keep the remaining G2 work on the critical path:

1. Complete split QA and freeze the leakage-safe manifest.
2. Ensure V1 loads through `interface.predict()` and the CLI with the real artifact and version recorded.
3. Record per-CWE/per-language metrics and unsupported/low-support classes; do not present provisional metrics as final.
4. Save the graph extraction subset, cache location, extraction failures, and node-embedding status for the GNN work.
5. Decide explicitly which incomplete Week 2 items are dropped: prioritize these over a broad V2 feature set, LLM baseline, and full corpus extraction.

### Phase A: build and deploy the V1 application (about 5 working days)

Do this after the Week 2 prerequisites are complete. Keep model work limited to V1 stability; this phase delivers a complete usable application before GNN experiments begin.

| Day | Focus | Work | Exit evidence |
|---|---|---|---|
| 1 | Contract and backend | Freeze the React-to-FastAPI request flow; implement health, supported languages, and snippet scan routes as thin wrappers over `shield_core.interface`. | A sample returns matching interface and API JSON; health and language routes work. |
| 2 | Frontend | Build React scan form, language selection, loading/error states, and result display for verdict, CWE, confidence, findings, and model version. | Local end-to-end scan uses the real V1 artifact. |
| 3 | Integration | Handle validation and API errors, confirm result serialization, enforce request size/time bounds, and show unsupported cases clearly. | Clean and vulnerable example snippets both render correctly. |
| 4 | Packaging and deployment | Build FastAPI and React containers; configure Docker Compose; deploy the same image to the demo host. | Public/staging URL responds to health and snippet scan. |
| 5 | Stabilization | Fix only blocking defects, rehearse the demo, verify startup from a clean checkout, and document deploy/rollback steps. | Stable V1 demo with recorded image/model tag and known limitations. |

**Phase A gate:** do not start the condensed GNN sprint until the deployed app can scan a snippet with V1, display the result and model version, and recover from API/model errors. If deployment is blocked by infrastructure, a clean local Compose demo is the temporary exit criterion; continue the deployment issue in parallel without blocking GNN work.

### Phase B: condensed Week 3 — GNN V2 (about 5 working days)

Once Phase A passes its gate, keep the application stable and dedicate the model track to the focused GNN experiment. Only integrate a GNN artifact after evaluation; until then the app continues to use V1.

| Day | Focus | Work | Exit evidence |
|---|---|---|---|
| 1 | Graph data validation | Validate PyG graphs against the frozen train/validation/test manifest; confirm label coverage, dropped-graph counts, and no split crossing. Cache node embeddings for this subset. | Graph dataset report and usable subset manifest saved. |
| 2 | Control model | Train one small graph-only baseline (variant A) with a fixed seed and manageable subset. | Reproducible baseline run logged. |
| 3 | GNN V2 | Train one CodeBERT-node-initialized GNN (variant B) on the same groups and labels; avoid architecture sweeps. | Checkpoint and run metadata saved. |
| 4 | Evaluation | Compare A, B, and V1 on identical eligible data; select only on validation; evaluate frozen test once. Report macro-F1 and per-CWE precision/recall/support and dropped-graph rates. | Evaluation table; no test-set tuning. |
| 5 | Decision and integration | Document whether V2 improves V1. If it passes the acceptance gate, register it as an optional model and smoke-test it through the app; otherwise keep V1 as primary. | Model card, recorded decision, and app still runs on V1 fallback. |

### Week 4 only if available: hardening, not expansion

Use remaining time for the highest-risk reliability gap: file/repository scanning only if the current interface supports it safely; otherwise improve scan errors, input limits, deployment health, evaluation/reporting, and one-click demo reliability. Add auth and persistence only if the app will be used beyond a controlled demo.

## 3. Five-person ownership (each owns one UI slice and its API/backend slice)

Each person is responsible for the vertical slice from React view to FastAPI route/service, plus their existing domain contribution. Share a single API branch/integration owner; each slice should use mocked API data until the contract is wired.

| Person | Frontend responsibility | Backend/model responsibility | Week 3 priority and handoff |
|---|---|---|---|
| **P1 — Hatem** | Scan history/status panel (local in-memory history; no database). | Input validation, language support endpoint, scan request limits, adapter checks against `interface.predict()`. Own data/split provenance and model-input assumptions. | Verify frozen data/split metadata and expose supported languages; hand off API schema examples to P5. |
| **P2 — Eyad** | Findings/evidence view: CWE, confidence, file/line if available, taint-path placeholder only when present. | GNN inference adapter behind the model registry/interface; graph checkpoint loading and graceful V1 fallback. | Train and package A/B checkpoints; hand off stable prediction call and artifact requirements to P3/P4. |
| **P3 — Atef** | Model/evaluation summary view: model version and compact per-CWE metrics page/table from saved report. | Reproducible training/evaluation entry point, MLflow run logging, calibration/metrics and V1-vs-GNN comparison. | Own GNN-vs-V1 evaluation and model card; hand off selected artifact and exact run config to P4. |
| **P4 — Bigad** | Result detail and fix status presentation, showing verification evidence without overstating “verified”. | FastAPI app, contract serialization, exception mapping, health route, registry selection and V1 fallback. | Own API integration and contract compatibility; hand off OpenAPI spec to P5. |
| **P5 — Maram** | React app shell, scan form, routing, responsive layout, API client and deploy-ready build. | Docker/Compose, environment configuration, CI image build, deployment and smoke-check instructions. | Own UI integration/deployment; hand off URL, env vars, and rollback instructions to the team. |

**Shared integration rules:** P4 owns API integration; P5 owns UI integration and release packaging. P2/P3 own model artifacts and evaluation. P1/P2 approve data/graph validity. No one edits the frozen interface silently; add a contract version/change note if a field is truly needed.

## 4. GNN V2: narrow experiment intended to improve on V1

“Better model” is the target, not a guaranteed outcome. The team should ship V1 as the default if GNN V2 fails the evidence gate.

1. **Keep the data fixed.** Use the same leakage-safe train/validation/test groups, label mapping, and eligible examples for V1 and GNN comparisons. Use validation to select; inspect the frozen test once.
2. **Use graph-only A as a control, then one proposed V2.** A: current shared node-type embeddings. B/V2: frozen CodeBERT embeddings for each node’s code text + shared node-type/edge-type embeddings + one small GAT or gated-GNN encoder + graph pooling + binary and CWE heads. Do not compare multiple architectures unless the first run is already complete.
3. **Keep scope tractable.** Use existing extracted graphs only; cap nodes at the already measured safe per-language setting (Python 750; C/C++ use the documented cap), batch by graph, skip/log invalid graphs, and cache node text embeddings. Begin with Python if graph-label coverage is the bottleneck; add C/C++ only when its cached subset is ready.
4. **Prevent shortcut gains.** Report length-only and V1 baselines. Compare macro-F1 and per-CWE precision/recall/support; report dropped graph rates and class coverage. Do not use synthetic samples in validation/test.
5. **Acceptance gate.** Promote V2 only if it beats V1 macro-F1 on the same validation data and does not materially damage supported high-priority CWE recall; confirm once on the frozen test and report confidence/support. Otherwise retain V1 as primary and present GNN as an experimental result.

Minimum artifacts: model checkpoint, config, fixed seed, dataset/split hash, graph converter/schema version, node embedding cache metadata, MLflow run (or saved run JSON if MLflow is unavailable), per-CWE evaluation table, and short model card with intended use and limitations.

## 5. Minimal MLOps and deployment checklist

- **Track:** extend existing `shield_core/tracking.py`; log seed, model/config, dataset and split hashes, graph converter version, metrics, and artifact path. Never log raw source code to a hosted tracker.
- **Package:** versioned local model artifacts and registry config; verify cold-start loading and V1 fallback. Do not commit large artifacts if existing storage/release mechanism is available.
- **Build:** pinned Python dependencies, FastAPI container, React static build, Compose health checks, environment-based API key/config only if auth is enabled.
- **Deploy:** deploy the same Compose/image artifact tested locally to the demo host; keep secrets outside the repo; expose only the app/API ports needed; record build tag and deployment date.
- **Operate:** `/v1/health`, bounded request size/time, useful server logs without code contents, one smoke scan, deployment rollback to prior image/model tag.
- **Reproduce:** one documented command for training/evaluation and one for local app startup; same model tag must appear in API results and MLflow/run manifest.

## 6. Demo scope and explicit cuts

**Must demo:** React UI; supported-language selector; pasted snippet; V1-backed result; model version and confidence; FastAPI health; deployed URL. After Phase B, add the reproducible GNN experiment record and measured V1 comparison to the demo.

**Only if already working:** graph/taint evidence in the finding, basic scan history for the current browser session.

**Defer:** repo URL/ZIP scanning and async job queue, login/OAuth, PostgreSQL, Redis/Celery, VS Code extension, automated fixes in the UI, CodeT5, Java, full-dataset graph extraction, augmentation, broad hyperparameter search, polished analytics dashboard.

## 7. Definition of done

- Clean checkout can build and start the app from the documented steps.
- Deployed UI can submit a snippet and display an API result from the real registered model.
- API reports health, supported languages, schema/model version, and actionable errors.
- V1 remains loadable as fallback; model version is visible to the user.
- GNN V2 has a reproducible run and a fair comparison against V1; results and limitations are written down, including a negative result if it does not win.
- No test-set-based tuning, no unsupported language claim, and no UI claim that a fix or result is “verified” without the configured evidence.

## 8. Decisions to log in the master plan

At the next team sync, add a dated row to `SHIELD_PLAN.md` Section 2 and a short entry in Section 15 for: the MVP deadline and cut line; React/FastAPI shipped during the compressed schedule; deployment target; GNN comparison/acceptance rule; and deferred product services. This companion file does not silently change the master plan's settled decisions.
