from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("http://localhost:5001/api/hello")
    return f"Frontend received: {response.json()['message']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
