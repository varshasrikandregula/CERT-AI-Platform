@app.get("/dashboard")
def dashboard():

    return {
        "status": "Dashboard Connected",
        "detection_engine": "Running",
        "soar_engine": "Running",
        "playbook_engine": "Running",
        "total_alerts": 5,
        "total_incidents": 3,
        "latest_incident": {
            "incident_id": 1001,
            "severity": "High"
        }
    }