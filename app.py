from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to my Flask API on Render!"})

@app.route("/hello")
def hello():
    return jsonify({"message": "Hello from Render!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
