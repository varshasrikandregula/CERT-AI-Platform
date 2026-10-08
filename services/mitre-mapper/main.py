from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MITRE Mapper")


class Alert(BaseModel):
    risk_level: str


@app.get("/")
def home():
    return {
        "status": "MITRE Mapper Running"
    }


@app.post("/map")
def map_to_mitre(alert: Alert):

    if alert.risk_level == "High":
        return {
            "technique_id": "T1078",
            "technique": "Valid Accounts",
            "tactic": "Defense Evasion"
        }

    elif alert.risk_level == "Medium":
        return {
            "technique_id": "T1110",
            "technique": "Brute Force",
            "tactic": "Credential Access"
        }

    else:
        return {
            "technique_id": "T1087",
            "technique": "Account Discovery",
            "tactic": "Discovery"
        }