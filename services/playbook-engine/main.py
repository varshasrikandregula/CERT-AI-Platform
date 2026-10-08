from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Playbook Engine")


class Incident(BaseModel):
    severity: str


@app.get("/")
def home():
    return {
        "status": "Playbook Engine Running"
    }


@app.post("/playbook")
def get_playbook(incident: Incident):

    if incident.severity == "High":
        return {
            "playbook": "High Risk Response",
            "action": "Isolate Host"
        }

    elif incident.severity == "Medium":
        return {
            "playbook": "Medium Risk Investigation",
            "action": "Investigate User Activity"
        }

    else:
        return {
            "playbook": "Low Risk Monitoring",
            "action": "Monitor Activity"
        }