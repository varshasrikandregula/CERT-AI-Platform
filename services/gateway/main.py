
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="CERT AI Gateway")

LANL_URL = "https://lanl-parser.onrender.com"
DETECTION_URL = "https://detection-engine-h2pb.onrender.com"
INCIDENT_URL = "https://incident-manager-bfzm.onrender.com"
SOAR_URL = "https://soar-engine.onrender.com"
MITRE_URL = "https://mitre-mapper.onrender.com"


def call_service(url: str, data: dict):
    try:
        response = requests.post(url, json=data, timeout=90)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Downstream service request failed: {exc}"
        )


@app.get("/")
def home():
    return {"status": "CERT AI Platform Running"}


@app.post("/parse")
def parse(data: dict):
    return call_service(f"{LANL_URL}/parse", data)


@app.post("/detect")
def detect(data: dict):
    return call_service(f"{DETECTION_URL}/detect", data)


@app.post("/incident")
def incident(data: dict):
    return call_service(f"{INCIDENT_URL}/incident", data)


@app.post("/respond")
def respond(data: dict):
    return call_service(f"{SOAR_URL}/respond", data)


@app.post("/map")
def map_attack(data: dict):
    return call_service(f"{MITRE_URL}/map", data)


@app.post("/pipeline")
def pipeline(data: dict):
    parsed = call_service(f"{LANL_URL}/parse", data)
    detection = call_service(f"{DETECTION_URL}/detect", parsed)
    incident = call_service(f"{INCIDENT_URL}/incident", detection)
    response = call_service(f"{SOAR_URL}/respond", incident)

    risk_level = detection.get("risk_level")
    if risk_level is None:
        raise HTTPException(
            status_code=502,
            detail="Detection Engine response did not contain risk_level"
        )

    mitre = call_service(
        f"{MITRE_URL}/map",
        {"risk_level": risk_level}
    )

    return {
        "parsed": parsed,
        "detection": detection,
        "incident": incident,
        "response": response,
        "mitre": mitre
    }
