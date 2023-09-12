import os
import json
import datetime

from dotenv import load_dotenv
from tqdm import tqdm

from news_listener import load_config, NewsListener
from keyword_extractor import KeywordExtractor
from sentiment_analyser import SentimentAnalyser


class CronJob:
    def __init__(self) -> None:
        self.__version__ = "0.1.1"
        self.config = load_config("./config.json")
        self.listener = NewsListener(
            key=os.getenv("NEWS_API_KEY"), domains=self.config["outlets"]
        )
        self.extractor = KeywordExtractor()
        self.analyser = SentimentAnalyser()

    def generate_sentiment(self, data, type=None):
        print(f"Calculating sentiments for {type}...")

        if type == "headlines":
            for article in tqdm(data["articles"]):
                article["sentiment"] = self.analyser(article["description"])

        elif type == "categorised":
            for category in tqdm(data["articles"]):
                for article in data["articles"][category]:
                    article["sentiment"] = self.analyser(article["description"])

        data["vartapratikriya"] = self.__version__
        data["last_active"] = str(datetime.datetime.now())
        return data

    def generate_keywords(self, data, k=10):
        print("Getting top keywords...")
        keywords = []
        for article in tqdm(data["articles"]):
            keywords.extend(self.extractor(article["title"]))

        word_counts = {}
        for string in keywords:
            word_counts[string] = word_counts.get(string, 0) + 1

        del word_counts[""]

        most_common = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        return {
            "vartapratikriya": self.__version__,
            "last_active": str(datetime.datetime.now()),
            "keywords": most_common[:k],
        }

    def run(self) -> None:
        headlines = self.listener.get_headlines()
        categorised = self.listener.get_categorised()

        # headlines_dict = self.generate_sentiment(data=headlines, type="headlines")
        # categorised_dict = self.generate_sentiment(data=categorised, type="categorised")
        top_dict = self.generate_keywords(data=headlines)

        # with open("../public/data/dump_headlines.json", "w") as json_file:
        #     json.dump(headlines_dict, json_file, indent=4, ensure_ascii=False)

        # with open("../public/data/dump_categorised.json", "w") as json_file:
        #     json.dump(categorised_dict, json_file, indent=4, ensure_ascii=False)

        with open("../public/data/dump_top.json", "w") as json_file:
            json.dump(top_dict, json_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    load_dotenv()
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACE_HUB_ACCESS_TOKEN")
    job = CronJob()
    job.run()
