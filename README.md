# CloudCostGuard  🚀

**Cloud cost spike detection & idle resource analysis** — a small toolkit that ingests cloud billing data, detects anomalies (cost spikes), explains contributors, and surfaces idle resources.

---

## 🔍 Features
- Detect daily cost spikes using rolling z-score and explain top contributing services.
- Identify idle or underutilized cloud resources.
- Interactive FastAPI backend (`/chat`) that answers questions about spikes and idle resources.
- Notebooks for data generation, spike detection, and idle-resource exploration.

---

## ⚙️ Quick start (PowerShell)
1. From the project root (folder containing `backend/`, `src/`, `data/`):
```powershell
# create + activate venv (one-time)
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\.venv\Scripts\Activate.ps1

# install dependencies
pip install --upgrade pip
pip install fastapi uvicorn pandas numpy pydantic matplotlib
```

2. Start the FastAPI server:
```powershell
# from project root
python -m uvicorn backend.main:app --reload --port 8000
```

3. Open the interactive API docs: `http://127.0.0.1:8000/docs` and try the `/chat` endpoint.

### Example requests
- curl:
```bash
curl -s -X POST http://127.0.0.1:8000/chat -H "Content-Type: application/json" -d '{"message":"is there a spike"}'
```
- PowerShell:
```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/chat -Method POST -Body (@{message='is there a spike'} | ConvertTo-Json) -ContentType 'application/json'
```

---

## 🗂 Project structure
- `backend/` — FastAPI app (`backend/main.py`) and related modules (moved from `data/backend`).
- `src/` — data loading, spike detection, idle detection, and explainers.
- `data/` — source notebooks and data:
  - `data/processed/` — processed CSVs (do not commit large processed files to GitHub)
  - `data/raw/` — original inputs
- `notebooks/` — analysis notebooks (moved from `data/notebooks`)

---

## 🧪 Notebooks
Open the notebooks in `notebooks/` to reproduce analyses:
- `01_synthetic_data_generation.ipynb` — generate synthetic billing data
- `02_cost_spike_detection.ipynb` — detect spikes and explain contributors
- `03_idle_resource_detection.ipynb` — find idle resources

---

## 📁 Data handling & git
- Do **not** commit large datasets into the repository. Add them to `.gitignore` or use Git LFS if necessary.
- Example `.gitignore` entries:
```
.venv/
data/processed/
.ipynb_checkpoints
```

---



