from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Load your API key from environment variable
API_KEY = os.environ.get("ORTHOS_API_KEY", "default-key")

@app.route("/")
def home():
    return "Orthos backend running 🚀"

@app.route("/verify-caller", methods=["POST"])
def verify_caller():
    data = request.json

    # Check if request has correct API key
    incoming_key = request.headers.get("x-api-key")
    if incoming_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    phone_number = data.get("phone_number")

    response = {
        "status": "verified",
        "phone_number": phone_number,
        "message": "Caller verified successfully"
    }

    return jsonify(response), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
