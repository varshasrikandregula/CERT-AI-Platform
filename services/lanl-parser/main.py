from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LANL Parser")


class LANLRecord(BaseModel):
    timestamp: int
    user: str
    source_computer: str
    destination_computer: str


@app.get("/")
def home():
    return {
        "status": "LANL Parser Running"
    }


@app.post("/parse")
def parse_lanl(record: LANLRecord):

    risk = "Low"

    if record.user.startswith("U620"):
        risk = "Medium"

    parsed_event = {
        "timestamp": record.timestamp,
        "user": record.user,
        "source_computer": record.source_computer,
        "destination_computer": record.destination_computer,
        "risk_level": risk,
        "status": "Parsed Successfully"
    }

    return parsed_event