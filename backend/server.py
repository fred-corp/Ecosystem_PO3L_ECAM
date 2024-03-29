import json
import os
import sys

import flask
import testBackend
from sim import simulateNextStep

root = os.path.join(
    os.path.dirname(os.path.abspath(__file__)).removesuffix("/backend"), "frontend"
)

examples = os.path.join(
    os.path.dirname(os.path.abspath(__file__)).removesuffix("/backend"),
    "ecosystemExampleFiles",
)


app = flask.Flask(__name__)


# Ping the API
@app.route("/pingAPI", methods=["GET"])
def pingAPI():
    return testBackend.testBackendCall()


# Main API
@app.route("/API", methods=["GET"])
def api():
    return ":)"


@app.route("/API/load", methods=["GET"])
def loadExample():
    file = open(os.path.join(examples, "example1.json"), "r+").read()
    return file

@app.route("/API/simulate", methods=["POST"])
def simulate():
    data = flask.request.form.getlist("json")
    ecoSymDict = json.loads(data[0])
    newEcoSymDict = simulateNextStep(ecoSymDict)
    return newEcoSymDict


# Homepage
@app.route("/", methods=["GET"])
def index():
    return flask.send_from_directory(root, "index/index.html")


# Simulate
@app.route("/simulate", methods=["GET"])
def simulate_page():
    return flask.send_from_directory(root, "simulate/index.html")


# About
@app.route("/about", methods=["GET"])
def about():
    return flask.send_from_directory(root, "about/index.html")


# Ping the website (used for GitHub Badge)
@app.route("/ping", methods=["GET"])
def ping():
    return "Website is up ⛄️"


# Route for js, css, images, ...
@app.route("/<path:path>", methods=["GET"])
def static_proxy(path):
    return flask.send_from_directory(root, path)


if __name__ == "__main__":
    app.run(debug=False, port=3000, host=sys.argv[1])
