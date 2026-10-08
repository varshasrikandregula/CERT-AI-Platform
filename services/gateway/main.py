from fastapi import FastAPI
import requests

app = FastAPI(title="CERT AI Gateway")


@app.get("/")
def home():
    return {"status": "CERT AI Platform Running"}


@app.post("/parse")
def parse(data: dict):
    return requests.post(
        "http://127.0.0.1:8006/parse",
        json=data
    ).json()


@app.post("/detect")
def detect(data: dict):
    return requests.post(
        "http://127.0.0.1:8007/detect",
        json=data
    ).json()


@app.post("/incident")
def incident(data: dict):
    return requests.post(
        "http://127.0.0.1:8008/incident",
        json=data
    ).json()


@app.post("/respond")
def respond(data: dict):
    return requests.post(
        "http://127.0.0.1:8009/respond",
        json=data
    ).json()


@app.post("/map")
def map_attack(data: dict):
    return requests.post(
        "http://127.0.0.1:8011/map",
        json=data
    ).json()
@app.post("/pipeline")
def pipeline(data: dict):

    parsed = requests.post(
        "http://127.0.0.1:8006/parse",
        json=data
    ).json()

    detection = requests.post(
        "http://127.0.0.1:8007/detect",
        json=parsed
    ).json()

    incident = requests.post(
        "http://127.0.0.1:8008/incident",
        json=detection
    ).json()

    response = requests.post(
        "http://127.0.0.1:8009/respond",
        json=incident
    ).json()

    mitre = requests.post(
        "http://127.0.0.1:8011/map",
        json={
            "risk_level": detection["risk_level"]
        }
    ).json()

    return {
        "parsed": parsed,
        "detection": detection,
        "incident": incident,
        "response": response,
        "mitre": mitre
    }