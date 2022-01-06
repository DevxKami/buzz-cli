from typing import List
from collections import Counter
import heapq
import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize


MAX_SENT_LENGTH = 30
SUMMARY_SENT_LENGTH = 1

def generate_count(content: str) -> Counter:
    content = content.lower()
    stop_words = stopwords.words('english')
    punctuation = string.punctuation + '\n'
    tokens = word_tokenize(content)
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [token for token in tokens if token not in punctuation]
    return Counter(tokens)


def generate_frequency(counters: Counter) -> dict:
    frequency = {}
    max_count = max(counters.values())
    for key in counters.keys():
        frequency[key] = counters[key] / max_count

    return frequency


def score_sentence(content: str, table: dict) -> dict:
    scores = {}
    for sentence in sent_tokenize(content):
        if len(sentence.split(' ')) < MAX_SENT_LENGTH:
            continue
        for word in nltk.word_tokenize(sentence.lower()):
            if word in table:
                score = scores.get(sentence, 0)
                score += table[word]
                scores[sentence] = score
    return scores


def summarize(content: str) -> str:
    counts = generate_count(content)
    table = generate_frequency(counts)
    scores = score_sentence(content, table)
    n_sentence = SUMMARY_SENT_LENGTH
    best_scores = heapq.nlargest(n_sentence, scores, key=scores.get)
    return ' '.join(best_scores)
