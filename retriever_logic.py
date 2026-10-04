import json
import re


def load_corpus():
    with open("data/corpus.json", "r", encoding="utf-8") as file:
        return json.load(file)


def retrieve_evidence(question: str, top_k: int = 3):
    corpus = load_corpus()

    question_words = set(re.findall(r"\b\w+\b", question.lower()))

    scored_sources = []

    for source in corpus:
        text_words = set(
            re.findall(r"\b\w+\b", source["text"].lower())
        )

        score = sum(
            1 for word in question_words
            if len(word) > 3 and word in text_words
        )

        scored_sources.append((score, source))

    scored_sources.sort(key=lambda x: x[0], reverse=True)

    return [
        source
        for score, source in scored_sources[:top_k]
        if score > 0
    ]