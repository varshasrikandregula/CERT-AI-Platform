from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI(title="Incident Manager")


class Alert(BaseModel):
    timestamp: int
    user: str
    source_computer: str
    destination_computer: str
    risk_level: str
    alert: bool


@app.get("/")
def home():
    return {
        "status": "Incident Manager Running"
    }


@app.post("/incident")
def create_incident(alert_data: Alert):

    if not alert_data.alert:
        return {
            "message": "No incident created"
        }

    incident_id = str(uuid.uuid4())[:8]

    return {
        "incident_id": incident_id,
        "severity": alert_data.risk_level,
        "user": alert_data.user,
        "status": "Open"
    }