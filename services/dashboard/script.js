fetch("http://127.0.0.1:8005/dashboard")
.then(response => response.json())
.then(data => {

    document.getElementById("detection").innerText =
        data.detection_engine;

    document.getElementById("soar").innerText =
        data.soar_engine;

    document.getElementById("playbook").innerText =
        data.playbook_engine;

    document.getElementById("alerts").innerText =
        data.total_alerts;

    document.getElementById("incidents").innerText =
        data.total_incidents;
});