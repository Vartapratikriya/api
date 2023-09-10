import os
import argparse

from dotenv import load_dotenv
from transformers import pipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="huggingface-cli",
        description="Simple CLI to get prompt results from Huggingface-hub models",
        epilog=":)",
    )
    parser.add_argument("--prompt")
    args = parser.parse_args()
    load_dotenv()
    token = os.getenv("HUGGINGFACE_HUB_ACCESS_TOKEN")

    pipe = pipeline(
        "text-classification",
        model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis",
    )

    print(pipe(args.prompt))
