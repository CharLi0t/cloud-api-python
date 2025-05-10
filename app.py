from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to my Flask API on Render!"})

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from Render!"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

@app.route("/api/status")
def status():
    return jsonify({"status": "running", "service": "flask-api", "version": "1.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
