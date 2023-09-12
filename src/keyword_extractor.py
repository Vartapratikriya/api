import os
import json

from tqdm import tqdm

from typing import List
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub


class Keyword_extractor:
    def __init__(self) -> None:
        pass

        self.llm = HuggingFaceHub(
            repo_id="Voicelab/vlt5-base-keywords", task="text2text-generation"
        )

    def __call__(self, string: str = None) -> List[str]:
        return self.llm.predict(string).split(",")
