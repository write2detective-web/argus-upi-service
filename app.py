import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "active", "service": "ARGUS UPI OSINT Wrapper"})

@app.route("/lookup", methods=["POST"])
def lookup():
    data = request.get_json() or {}
    query_value = data.get("query") or data.get("upi_id") or data.get("phone")

    if not query_value:
        return jsonify({"error": "Missing query parameter (upi_id or phone)"}), 400

    # Placeholder structured response for ARGUS integration
    return jsonify({
        "query": query_value,
        "status": "success",
        "message": "Lookup request received by remote server",
        "risk_score": 15,
        "verified": False
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
