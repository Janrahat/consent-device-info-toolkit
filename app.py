from flask import Flask, render_template, request, jsonify
from datetime import datetime, timezone
from pathlib import Path
import json

app = Flask(__name__)
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "consented_demo_data.jsonl"

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/collect")
def collect():
    # This demo stores only fields explicitly submitted by the visitor.
    # It deliberately does not record IP addresses, headers, or fingerprints.
    data = request.get_json(silent=True) or {}
    if data.get("consent") is not True:
        return jsonify({"error": "Explicit consent is required."}), 400

    allowed = {
        "platform", "screen", "language", "timezone",
        "latitude", "longitude", "accuracy"
    }
    record = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "consent": True,
        **{key: data.get(key) for key in allowed if key in data}
    }
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return jsonify({"status": "saved", "message": "Consent-based demo data saved."})

@app.get("/live")
def live():
    # Local demo dashboard. Do not expose this endpoint to the public internet.
    if not LOG_FILE.exists():
        return "<h1>Consent-based demo dashboard</h1><p>No consented demo records yet.</p>"
    rows = []
    for line in LOG_FILE.read_text(encoding="utf-8").splitlines()[-100:]:
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return "<h1>Consent-based demo dashboard</h1><pre>" + \
           json.dumps(rows, indent=2, ensure_ascii=False) + "</pre>"

if __name__ == "__main__":
    print("Consent-based Device Info Demo")
    print("Open http://127.0.0.1:8080")
    print("Dashboard: http://127.0.0.1:8080/live (local testing only)")
    app.run(host="127.0.0.1", port=8080, debug=False)
