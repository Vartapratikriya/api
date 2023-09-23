import os
import json
import requests

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
    return jsonify(
        requests.get(
            "https://vartapratikriya.github.io/vartapratikriya-cron-job/src/config.json"
        ).json()
    )


@app.route("/articles/topKeywords")
def top():
    response = db["top_keywords"].find(request.args.to_dict(), {"_id": 0})
    articles = [article for article in response]
    return jsonify({"articles": articles})


@app.route("/articles/sentiment")
def sentiment():
    filter_by = request.args["filterBy"]
    config = requests.get(
        "https://vartapratikriya.github.io/vartapratikriya-cron-job/src/config.json"
    ).json()

    if filter_by == "language":
        response = db["headlines"].find({}, {"_id": 0})
        result = {language: 0.0 for language in config["outlets"].keys()}
        for article in response:
            lang = article["language"]
            if article["sentiment"] == "positive":
                result[lang] += article["sentiment_conf"]
            elif article["sentiment"] == "negative":
                result[lang] -= article["sentiment_conf"]

    elif filter_by == "category":
        response = db["categorised"].find({}, {"_id": 0})
        result = {category: 0.0 for category in config["categories"]}
        for article in response:
            category = article["category"]
            if article["sentiment"] == "positive":
                result[category] += article["sentiment_conf"]
            elif article["sentiment"] == "negative":
                result[category] -= article["sentiment_conf"]

    return jsonify(result)


@app.route("/articles/fact")
def fact():
    filter_by = request.args["filterBy"]
    config = requests.get(
        "https://vartapratikriya.github.io/vartapratikriya-cron-job/src/config.json"
    ).json()

    if filter_by == "language":
        response = db["headlines"].find({}, {"_id": 0})
        result = {language: 0.0 for language in config["outlets"].keys()}
        for article in response:
            lang = article["language"]
            if article["fact"] == "TRUE":
                result[lang] += article["fact_conf"]
            elif article["fact"] == "FAKE":
                result[lang] -= article["fact_conf"]

    elif filter_by == "category":
        response = db["categorised"].find({}, {"_id": 0})
        result = {category: 0.0 for category in config["categories"]}
        for article in response:
            category = article["category"]
            if article["fact"] == "TRUE":
                result[category] += article["fact_conf"]
            elif article["fact"] == "FAKE":
                result[category] -= article["fact_conf"]

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
