import os
import argparse

from dotenv import load_dotenv
from googletrans import Translator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="bard-cli",
        description="Simple CLI to get translations results from Google's Tanslate API",
        epilog=":)",
    )
    parser.add_argument("--text")
    parser.add_argument("--dest")
    args = parser.parse_args()

    translator = Translator()
    print(translator.translate(text=args.text, dest=args.dest))
