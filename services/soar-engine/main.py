from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SOAR Engine")


class Incident(BaseModel):
    incident_id: str
    severity: str
    user: str
    status: str


@app.get("/")
def home():
    return {
        "status": "SOAR Engine Running"
    }


@app.post("/respond")
def respond(incident: Incident):

    if incident.severity == "High":
        playbook = "High Risk Response"
        action = "Isolate Host"

    else:
        playbook = "Standard Investigation"
        action = "Monitor Activity"

    return {
        "incident_id": incident.incident_id,
        "playbook": playbook,
        "action": action,
        "status": "Executed"
    }