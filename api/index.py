import json

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def root():
    return jsonify(
        {
            "vartapratikriya": "v0.1.1",
            "status": "ok",
        }
    )


@app.route("/articles/top")
def top():
    with open("public/data/dump_top.json") as f:
        dump = json.load(f)
    return jsonify(dump)


@app.route("/articles/headlines")
def headlines():
    with open("public/data/dump_headlines.json") as f:
        dump = json.load(f)
    return jsonify(dump)


@app.route("/articles/categories")
def categories():
    args = request.args
    with open("public/data/dump_categorised.json") as f:
        dump = json.load(f)
    keyword = args["category"]
    if keyword == "all":
        return jsonify(dump)
    else:
        dump["articles"] = dump["articles"][keyword.lower()]
        return jsonify(dump)


if __name__ == "__main__":
    app.run(debug=True)
