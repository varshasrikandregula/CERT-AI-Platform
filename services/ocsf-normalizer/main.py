from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "OCSF Normalizer Running"}

@app.post("/normalize")
def normalize(event: dict):

    ocsf_event = {
        "class_name": "Process Activity",
        "activity_name": "Process Start",
        "process_name": event.get("Image"),
        "user": event.get("User"),
        "host": event.get("Computer")
    }

    return ocsf_event