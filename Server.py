from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store latest location
locations = {}

@app.route("/")
def home():
    return "GPS Tracking Backend is Running"

@app.route("/update", methods=["POST"])
def update():
    data = request.json

    device_id = data.get("device_id")
    lat = data.get("lat")
    lng = data.get("lng")
    speed = data.get("speed")

    if not device_id:
        return "Missing device_id", 400

    locations[device_id] = {
        "lat": lat,
        "lng": lng,
        "speed": speed,
        "time": datetime.utcnow().isoformat()
    }

    return "ok"

@app.route("/location/<device_id>")
def location(device_id):
    if device_id not in locations:
        return "no data", 404
    return jsonify(locations[device_id])

app.run(host="0.0.0.0", port=5000)
