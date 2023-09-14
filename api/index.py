import os
import json

from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
cors = CORS(app)


app = Flask(__name__)

db = MongoClient(
    f"mongodb+srv://007rajdeepghosh:{os.getenv('MONGO_DB_PASSWORD')}@api.rj03kl4.mongodb.net/?retryWrites=true&w=majority"
)["api"]


@app.route("/")
def root():
    response = db["status"].find_one({})
    del response["_id"]
    return jsonify(response)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        "public/",
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/config")
def config():
    with open("public/config.json") as f:
        dump = json.load(f)
    return jsonify(dump)


@app.route("/articles/top_keywords")
def top():
    response = db["top_keywords"].find(request.args.to_dict(), {"_id": 0})
    articles = [article for article in response]
    return jsonify({"articles": articles})


@app.route("/articles/sentiment")
def sentiment():
    filter_by = request.args["filter_by"]
    with open("public/config.json") as f:
        config = json.load(f)

    if filter_by == "language":
        response = db["headlines"].find({}, {"_id": 0})
        result = {language: 0.0 for language in config["outlets"].values()}
        for article in response:
            sen = article["sentiment"]
            lang = article["language"]
            if sen["label"] == "positive":
                result[lang] += sen["score"]
            elif sen["label"] == "negative":
                result[lang] -= sen["score"]

    elif filter_by == "category":
        response = db["categorised"].find({}, {"_id": 0})
        result = {category: 0.0 for category in config["categories"]}
        for article in response:
            sen = article["sentiment"]
            category = article["category"]
            if sen["label"] == "positive":
                result[category] += sen["score"]
            elif sen["label"] == "negative":
                result[category] -= sen["score"]

    return jsonify(result)


@app.route("/articles/headlines")
def headlines():
    response = db["headlines"].find(request.args.to_dict(), {"_id": 0})
    articles = [article for article in response]
    return jsonify({"articles": articles})


@app.route("/articles/categories")
def categories():
    response = db["categorised"].find(request.args.to_dict(), {"_id": 0})
    articles = [article for article in response]
    return jsonify({"articles": articles})


@app.after_request
def cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == "__main__":
    app.run(debug=True)
