from flask import Flask, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/postData", methods=["POST"])
def postData():
    print("data", request.json)
    return "It worked!"

@app.route("/getData", methods=["GET"])
def getData():
    person = {
        "name": "Cole Corson",
        "age": 21
    }

    return json.dumps(person)