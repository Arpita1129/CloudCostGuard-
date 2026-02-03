def detect_intent(message: str):
    msg = message.lower()

    if "spike" in msg or "increase" in msg or "high" in msg:
        return "spike"

    if "idle" in msg or "waste" in msg or "unused" in msg:
        return "idle"

    if "summary" in msg:
        return "summary"

    return "unknown"
