import argparse

from transformers import pipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="bard-cli",
        description="Simple CLI tool to use a qa-llm model",
        epilog=":)",
    )
    parser.add_argument("--question")
    parser.add_argument("--context")
    args = parser.parse_args()

    pipe = pipeline(
        "question-answering",
        model="deepset/roberta-base-squad2",
        tokenizer="deepset/roberta-base-squad2",
    )

    print(pipe({"question": args.question, "context": args.context})["answer"])
