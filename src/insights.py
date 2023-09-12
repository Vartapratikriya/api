import os
import json
import datetime

from tqdm import tqdm
from dotenv import load_dotenv

from typing import Dict

from keyword_extractor import Keyword_extractor


class News_insights:
    def __init__(self, data: Dict) -> None:
        self.data = data
        self.extractor = Keyword_extractor()

    def get_keywords(self, k) -> Dict:
        print("Getting top keywords...")
        keywords = []
        for article in tqdm(self.data["articles"]):
            keywords.extend(self.extractor(article["title"]))

        word_counts = {}
        for string in keywords:
            word_counts[string] = word_counts.get(string, 0) + 1

        most_common = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        return {
            "insights": "v0.1.0",
            "generated_at": str(datetime.datetime.now()),
            "keywords": most_common[:k],
        }


if __name__ == "__main__":
    load_dotenv()
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACE_HUB_ACCESS_TOKEN")
    with open("/data/dump_headlines.json") as f:
        dump = json.load(f)
    insights = News_insights(data=dump)

    with open("/data/dump_top.json", "w") as json_file:
        json.dump(
            insights.get_keywords(10),
            json_file,
            indent=4,
            ensure_ascii=False,
        )
