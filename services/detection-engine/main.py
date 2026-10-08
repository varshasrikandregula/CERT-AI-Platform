from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Detection Engine")


class Event(BaseModel):
    timestamp: int
    user: str
    source_computer: str
    destination_computer: str


@app.get("/")
def home():
    return {"status": "Detection Engine Running"}


@app.post("/detect")
def detect(event: Event):

    risk_level = "Low"
    alert = False

    # Demo detection rules
    if event.destination_computer == "C1003":
        risk_level = "High"
        alert = True

    elif event.user.startswith("U620"):
        risk_level = "Medium"
        alert = True

    return {
        "timestamp": event.timestamp,
        "user": event.user,
        "source_computer": event.source_computer,
        "destination_computer": event.destination_computer,
        "risk_level": risk_level,
        "alert": alert
    }