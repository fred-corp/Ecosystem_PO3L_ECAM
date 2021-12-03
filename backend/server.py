import os

import flask
import testBackend

root = os.path.join(
    os.path.dirname(os.path.abspath(__file__)).removesuffix("/backend"), "frontend"
)

app = flask.Flask(__name__)


@app.route("/API", methods=["GET"])
def api():
    return testBackend.testBackendCall()


@app.route("/", methods=["GET"])
def index():
    return flask.send_from_directory(root, "index.html")


@app.route("/ping", methods=["GET"])
def ping():
    return "Website is up ⛄️"


@app.route("/<path:path>", methods=["GET"])
def static_proxy(path):
    return flask.send_from_directory(root, path)


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")
