from __future__ import unicode_literals
from hazm import *
import json


normalizer = Normalizer()
stemmer = Stemmer()
lemmatizer = Lemmatizer()

with open("IR_data_news_12k.json", "r") as read_file:
    data = json.load(read_file)


def remove_stop_words(words):
    temp_words = words
    j = 0
    for i in range(0, len(temp_words)):
        if temp_words[i] in stopwords_list():
            words.pop(j)
        else:
            j += 1

    return words


def preprocess(text):
    text = normalizer.normalize(text)
    # print(text)
    words = word_tokenize(text)
    # print(words)
    words = remove_stop_words(words)
    print(words)

    for i in range(0, len(words)):
        words[i] = lemmatizer.lemmatize(words[i])

    return words


for i in data:
    data[i]['title'] = preprocess(data[i]['title'])
    data[i]['content'] = preprocess(data[i]['content'])

