import requests
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, world!"

@app.route('/test', methods=["GET"])
def dummy_call():
    endpoint = "http://10.244.2.42:80/nnrf-nfm/v1/nf-instances"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.get(endpoint, headers=headers)
    print(response.status_code)
    print(response.content)

    return response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)