"""Simple pre-run checker for the backend.
Checks: imports, data file exists.
Exit code 0 on success, non-zero on failure.
"""
import sys
import os

errors = []

try:
    from backend.chat import detect_intent
except Exception as e:
    errors.append(f"Failed to import backend.chat: {e}")

try:
    import src.data_loader as dl
    import src.spike_detection as sd
    import src.idle_detection as idd
    import src.explainers as ex
except Exception as e:
    errors.append(f"Failed to import src modules: {e}")

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "processed", "cloud_billing_synthetic.csv")
if not os.path.exists(DATA_PATH):
    errors.append(f"Data file not found: {DATA_PATH}")

if errors:
    print("CHECK FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(2)

print("CHECK OK")
sys.exit(0)
