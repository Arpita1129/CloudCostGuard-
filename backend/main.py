from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from src.data_loader import load_billing_data
from src.spike_detection import compute_daily_cost, detect_spikes
from src.idle_detection import detect_idle_resources
from src.explainers import explain_spike, explain_idle
from backend.chat import detect_intent

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],   # THIS IS IMPORTANT
    allow_headers=["*"],
)

DATA_PATH = "data/processed/cloud_billing_synthetic.csv"
df = load_billing_data(DATA_PATH)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    intent = detect_intent(req.message)

    if intent == "spike":
        daily = compute_daily_cost(df)
        spikes = detect_spikes(daily)

        if spikes.empty:
            return {"reply": "No significant cost spikes detected."}

        last_spike_date = spikes.iloc[-1]["date"].date()
        return {"reply": explain_spike(last_spike_date)}

    if intent == "idle":
        idle = detect_idle_resources(df)

        if idle.empty:
            return {"reply": "No major idle resources detected."}

        return {"reply": explain_idle(idle.iloc[0])}

    if intent == "summary":
        return {
            "reply": (
                "Your cloud environment shows occasional cost spikes "
                "and underutilized resources that can be optimized."
            )
        }

    return {
        "reply": (
            "I can help with cloud cost spikes, idle resources, "
            "or a cost summary."
        )
    }
