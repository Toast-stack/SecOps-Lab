from flask import Flask, render_template, jsonify
import json
from CorrelationStation import process_logs

app = Flask(__name__)

@app.route('/')
def index():
    # Process logs to find alerts and pas them to the HTML template
    alerts = process_logs()
    return render_template('index.html', alerts=alerts)

@app.route("/logs")
def logs():
    # Provide an API endpoint to return all logs as JSON

    logs_list = []
    with open("logs.jsonl", "r") as f:
        for line in f:
            try:
                logs_list.append(json.loads(line))
            except json.decoder.JSONDecodeError:
                continue
    return jsonify(logs_list)

if __name__ == "__main__":
    app.run(debug=True)