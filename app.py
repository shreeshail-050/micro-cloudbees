from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/todos")
def todos():
    return jsonify([
        {"id": 1, "task": "Learn CloudBees"},
        {"id": 2, "task": "Deploy to Kubernetes"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
