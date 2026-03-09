from flask import Flask
from detection_engine import analyze_logs

app = Flask(__name__)

@app.route("/")

def dashboard():

    alerts = analyze_logs()

    html = "<h1>SOC Alerts Dashboard</h1>"

    for log, alert in alerts:

        html += f"<p>{log} → {alert}</p>"

    return html


app.run(port=5000)