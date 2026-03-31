# MLOpsGuide.md

This guide is a practical learning plan for becoming job-ready in **MLOps / ML-DevOps**—especially if you’re coming from **DevOps (platform/CI/CD/containers)**.

It’s mapped to the most common MLOps interview question themes:
- ML lifecycle correctness
- Model versioning / promotion / rollback
- Experiment tracking + traceability (DVC + MLflow)
- Serving reliability (API contracts, validation, latency)
- Monitoring + alerting (data + model + system)
- CI/CD for ML pipelines (train-eval-deploy)
- Scenario drills (debugging when things go wrong)

---

## 0) What you already have (in this repo)

You currently have:
- A **DVC pipeline** in `dvc.yaml` with stages:
  - `prepare`: generates `data/iris.csv`
  - `train`: trains `model.pkl` and writes `metrics.json`
- **MLflow usage** inside `src/train.py` (logs metric + model)
- A **FastAPI** service in `api/app.py` that loads `model.pkl` and exposes:
  - `GET /` health
  - `POST /predict` prediction endpoint
- A **Dockerfile** that runs the FastAPI app
- An **Azure Pipeline** (`azure-pipelines.yaml`) that installs deps, runs `dvc repro`, evaluates, and builds a docker image

Practical implication: you can run a full “train → evaluate → serve” loop locally and then turn it into portfolio-quality work.

### Small repo gotcha to be aware of
Your training/evaluation scripts include a filename mismatch:
- your repo has `src/evalute.py`
- your Azure pipeline calls `python src/evaluate.py`

When you do the “pipeline end-to-end” practical labs, fix or reconcile that mismatch in your local notes so your results are consistent.

---

## 1) Setup checklist (practical)

### 1.1 Install tools
You’ll want these locally (versions pinned ideally in your real setup):
- Python 3.10+
- `dvc`
- `mlflow`
- Docker (for serving validation)
- `kubectl` (optional now; later for K8s concepts)
- `pytest` (optional; later for tests)

### 1.2 Create a local runbook folder (recommended)
Create a folder like `runbooks/` (optional) where you keep:
- command history
- screenshots/logs from failing runs
- final artifacts (model version, metrics snapshot)

Deliverable for interviews: “I can reproduce the run and explain the logs.”

### 1.3 Quick start commands (for the practical labs)
Use this as a starting point in your terminal:

```powershell
pip install -r requirements.txt

# If your repo isn't initialized for DVC yet, do:
# dvc init

# Re-run the pipeline that produces:
# data/iris.csv, model.pkl, metrics.json
dvc repro

# Evaluate (note: your repo currently has src/evalute.py)
python src/evalute.py

# Build and run the API container
docker build -t iris-api .
docker run -p 8000:8000 iris-api

# Basic smoke test
curl http://localhost:8000/
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "[5.1,3.5,1.4,0.2]"
```

---

## 2) Lab 1: Reproducibility + pipeline basics (Interview: “How do you make training reproducible?”)

### Goal
Prove that the same pipeline steps produce the same outputs (or at least trace the differences).

### Do (practical)
1. Run the full DVC pipeline from scratch.
2. Confirm outputs exist where the pipeline expects them (look for `data/iris.csv`, `model.pkl`, `metrics.json`).
3. Record:
   - command used
   - produced artifact files
   - metric values

### What to explain in interview
- “Reproducibility” includes: pinned dependencies, data versioning, deterministic splits, and recording training config.
- DVC tells you *what data/artifacts correspond to what code*; MLflow tells you *what experiment/run happened*.

### Deliverable
- A short doc section in your notes: “Reproducibility run log”.

---

## 3) Lab 2: Data leakage + evaluation correctness (Interview: “What is leakage? Why is offline accuracy unreliable?”)

### Goal
Understand how evaluation can lie—and how you prevent it.

### Do (practical)
1. Look at the split logic in training (train/validation/test).
2. Identify where leakage can occur:
   - preprocessing done before split
   - feature engineering using full dataset statistics
   - selecting the best model on the test set
3. Change your approach mentally:
   - fit preprocessors only on train
   - keep test untouched until final evaluation
4. If you’re using time-dependent data later: enforce time-based splits.

### Repo tie-in (what to examine)
- `src/train.py` uses train/test split and logs `accuracy`.

### Deliverable
- A “leakage checklist” you can recite in interviews.

---

## 4) Lab 3: Metric gating + quality gates (Interview: “How do you gate promotion?”)

### Goal
Turn metrics into a decision system.

### Do (practical)
1. Understand what the evaluation step does:
   - It reads `metrics.json`
   - It fails the pipeline if accuracy is below threshold
2. Improve your reasoning:
   - accuracy alone is not enough for imbalanced or cost-sensitive problems
   - choose metric(s) that align with business risk
3. Record two runs:
   - one passing your threshold
   - one failing by intentionally worsening setup (e.g., fewer estimators) *in your local experiments*

### What to explain in interview
- “Offline gates reduce risk but don’t guarantee production success.”
- You still need rollout controls + monitoring.

### Deliverable
- A sample “quality gate policy” statement:
  - metrics to check
  - threshold rules
  - what action happens on fail

---

## 5) Lab 4: Model promotion + rollback (Interview: “How do you promote and rollback?”)

### Goal
Have a clear promotion story: dev → staging → prod.

### Do (practical)
1. Define your environments:
   - `dev`: any trained model that passes minimal checks
   - `staging`: candidate model validated with additional tests + shadow traffic
   - `prod`: only models that passed final approval
2. Decide promotion mechanism:
   - A “candidate” is registered
   - promotion happens after passing acceptance tests
3. Practice rollback strategy:
   - keep the last known-good model artifact
   - version model in registry
   - rollout can be reverted quickly (container config points to old model version)

### Repo tie-in
- Today you directly load `model.pkl` at API startup.
- For real MLOps, you’ll want to load by a versioned artifact identifier (even if it’s just a filename convention).

### Deliverable
- A one-page “promotion + rollback” flow diagram in your notes.

---

## 6) Lab 5: MLflow traceability (Interview: “How do you track experiments and reproduce runs?”)

### Goal
Answer: “Given a model in production, how do you find exactly how it was trained?”

### Do (practical)
1. Identify what `src/train.py` logs to MLflow:
   - experiment name
   - metrics (accuracy)
   - model artifact
2. Practice what an auditor would do:
   - find the run
   - extract parameters
   - link to the exact code commit / config (you can document how you’d do that)

### What to explain in interview
- DVC and MLflow solve different problems:
  - DVC: reproducible data/artifact pipeline lineage
  - MLflow: experiment metadata + model artifacts per run

### Deliverable
- “Trace a model” script outline in notes (even if you don’t code it yet):
  - find run
  - verify metric gate
  - find artifact/model version

---

## 7) Lab 6: Serving contract + API validation (Interview: “How do you ensure inference is safe?”)

### Goal
Treat inference as an API product with strict input/output guarantees.

### Do (practical)
1. Define the request schema for `/predict`:
   - expected feature count/order
   - allowed ranges
   - type checks
2. Add a mental “input validation plan”:
   - validate JSON body type
   - validate length of features
   - validate numeric coercion + bounds
3. Plan for graceful failure:
   - return 400 for invalid input
   - log structured errors
   - do not crash the server

### Repo tie-in
- `api/app.py` currently accepts `features: list` and directly calls `model.predict([features])`.

### Deliverable
- A short “API contract” document:
  - request/response examples
  - error cases
  - how you validate inputs

---

## 8) Lab 7: Latency + reliability drills (Interview: “How do you meet performance targets?”)

### Goal
Be able to reason about production constraints.

### Do (practical)
1. Load test conceptually:
   - measure p50/p95 latency for predict calls
   - measure error rate under load
2. Identify bottlenecks:
   - model loading at startup vs per-request
   - serialization overhead
   - CPU usage vs memory
3. Reliability practices:
   - timeouts
   - circuit breaking (if dependencies exist)
   - concurrency settings

### Deliverable
- A “latency + reliability checklist” you can discuss.

---

## 9) Lab 8: Monitoring (system + ML) (Interview: “What monitoring do you set up?”)

### Goal
Know what to alert on and how to diagnose.

### Do (practical)
Divide monitoring into 3 categories:

1. System metrics (always required)
   - request rate
   - error rate (5xx)
   - latency p95/p99
   - CPU/memory usage

2. Data/input health
   - invalid request count (schema violations)
   - missing fields
   - unexpected feature distribution (basic drift checks)

3. Model performance
   - offline accuracy is not enough
   - if labels arrive later: compute accuracy later and track it
   - if labels not available: track proxy signals and drift

### Repo tie-in
- There is no monitoring code yet; this is an interview topic you must explain clearly.

### Deliverable
- A monitoring plan you can show in interview:
  - metrics list
  - dashboards
  - alert thresholds
  - runbook steps

---

## 10) Lab 9: CI/CD for ML (Interview: “How do you structure CI/CD?”)

### Goal
Build the ML pipeline as a reproducible build artifact pipeline.

### Do (practical)
Your CI/CD should have stages like:
1. Lint/unit tests (code quality)
2. Data checks (schema, missing values, row counts)
3. Train (produce artifacts)
4. Evaluate (metric gates)
5. Build image (or deploy job)
6. Deploy to environment
7. Smoke test the API

### Repo tie-in
- `azure-pipelines.yaml` already does:
  - install dependencies
  - `dvc repro`
  - run evaluation
  - build Docker image

### Deliverable
- A “pipeline contract” diagram:
  - input triggers
  - output artifacts
  - promotion conditions

---

## 11) Lab 10: Scenario drills (Interview: “Debug this failure”)

### Goal
Be ready for incident-style questions.

### Common scenarios to practice
1. Training passes but production accuracy drops
   - likely data drift, preprocessing mismatch, feature order mismatch, label shift
2. Pipeline fails in CI but works locally
   - dependency pinning mismatch, path issues, missing env vars, non-deterministic split
3. Model serving crashes after deployment
   - model file missing, wrong artifact name, incompatible serialization version
4. Latency spikes
   - cold starts, resource limits, serialization overhead, concurrency misconfig

### Deliverable
- For each scenario: your 5-step troubleshooting plan.

---

## 12) Portfolio deliverables (what to show recruiters)

You don’t need many projects—one solid end-to-end one is enough.
For each project, your README/notes should include:
- How to reproduce the pipeline
- Artifact lineage: which files are produced by which stage
- What MLflow run corresponds to the served model
- Quality gate policy
- Deployment strategy + rollback plan
- Monitoring plan + alert thresholds
- A couple of debug stories you learned from

---

## 13) Suggested timeline (practical)

If you do ~2-3 hours/day:
- Day 1-2: run DVC pipeline end-to-end + document outputs
- Day 3-4: metric gating + explain evaluation correctness
- Day 5-6: promotion/rollback story (even as a design doc)
- Day 7-8: MLflow traceability drill
- Day 9-10: serving contract + reliability reasoning
- Day 11-12: monitoring plan + alert/runbook write-up
- Day 13-14: CI/CD pipeline improvement plan + scenario drills

---

## 14) Questions for you (so I can tailor the next plan)
1. Are you targeting roles more on **Azure ML managed services**, or **Kubernetes/platform** MLOps, or **pipeline engineering**?
2. Do you want to focus on **real-time inference** or **batch scoring** first?
3. How much time can you spend per day for 2-3 weeks?

