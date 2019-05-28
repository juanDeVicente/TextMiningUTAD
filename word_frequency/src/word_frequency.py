import os
import nltk
from nltk.corpus import stopwords
import sys


def word_frequency(text, stopwords_language='english'):
    '''
    :param text: the text that is gonna be analyzed
    :param stopwords_language: language of the stopwords
    :return: list of (word, number of times that the word appears in the text/ number of words in the text without stopwords * 100)
    the rounding: one decimal and upper
    the list will be order by most used word to least
    '''

    nltk.data.path.append(os.path.dirname(__file__) + '/nltk_data')
    if not isinstance(text, str) or not isinstance(stopwords_language, str):
        raise ValueError

    if text == '':
        return []

    text = text.strip()
    text = ' '.join(text.split())  # Remove all the spaces between words
    words = text.replace(",", "").replace(".", "").replace(":", "").replace(";", "").replace("?", "").replace("!", "") \
        .replace("¿", "").replace("¡", "")
    words = words.strip()

    if words == '':
        return []

    words = words.split(' ')  # Slit by words

    words = [word.lower() for word in words if word.lower() not in stopwords.words(stopwords_language)]

    words_count = {}

    words_total = len(words)

    for key in words:
        words_count[key] = words_count.get(key, 0) + 1
        # If the key exists it returns the value, else returns the second param

    if len(words_count) == 0:
        return []

    for key in words_count:
        words_count[key] = round((words_count[key] / words_total) * 100, 1)

    return sorted(words_count.items(), key=lambda x: x[1], reverse=True)  # Order by most used to least used


if __name__ == "__main__":

    print(word_frequency("hola adios hola", "spanish"))
