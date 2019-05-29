
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from unittest.mock import MagicMock

import requests


from twitter_api.src.twitter_api import twitter_word_count

def test_less_than_10_tweets():
    tweets = ['Hola buenas dias, me llamo Pepe', 'buenas noches', 'me llamo pepe']
    twc = twitter_word_count(None)
    twc.get_last_week_tweets = MagicMock(return_value=tweets)
    assert twc.get_most_used_words_and_tweets() == [['buenas', 22.2, ['Hola buenas dias, me llamo Pepe','buenas noches']],
                                                    ['llamo',22.2,['Hola buenas dias, me llamo Pepe','me llamo pepe']],
                                                    ['pepe', 22.2, ['Hola buenas dias, me llamo Pepe','me llamo pepe' ]],
                                                    ['hola', 11.1, ['Hola buenas dias, me llamo Pepe']],
                                                    ['dias', 11.1, ['Hola buenas dias, me llamo Pepe']],
                                                    ['noches', 11.1, ['buenas noches']]]

def test_more_than_10_tweets():
    tweets = ['Hola buenas dias, me llamo Pepe', 'buenas noches', 'me llamo pepe','pedro juan alberto sabado miercoles jueves']
    twc = twitter_word_count(None)
    twc.get_last_week_tweets = MagicMock(return_value=tweets)
    assert twc.get_most_used_words_and_tweets() == [['buenas', 13.3, ['Hola buenas dias, me llamo Pepe','buenas noches']],
                                                    ['llamo',13.3,['Hola buenas dias, me llamo Pepe','me llamo pepe']],
                                                    ['pepe', 13.3, ['Hola buenas dias, me llamo Pepe','me llamo pepe' ]],
                                                    ['hola', 6.7, ['Hola buenas dias, me llamo Pepe']],
                                                    ['dias', 6.7, ['Hola buenas dias, me llamo Pepe']],
                                                    ['noches', 6.7, ['buenas noches']],
                                                    ['pedro',6.7,['pedro juan alberto sabado miercoles jueves']],
                                                    ['juan', 6.7, ['pedro juan alberto sabado miercoles jueves']],
                                                    ['alberto', 6.7, ['pedro juan alberto sabado miercoles jueves']],
                                                    ['sabado',6.7, ['pedro juan alberto sabado miercoles jueves']]
                                                    ]

def test_none_tweets():
    tweets = []
    twc = twitter_word_count(None)
    twc.get_last_week_tweets = MagicMock(return_value=tweets)
    with pytest.raises(TypeError):
        twc.get_most_used_words_and_tweets()


def test_boolean():
    twc = twitter_word_count(None)
    twc.get_last_week_tweets = MagicMock(return_value=True)
    with pytest.raises(TypeError):
        twc.get_most_used_words_and_tweets()


def test_stop_words_tweet():
    tweets = ['ella el', 'nosotros y ellos', 'un una', 'unos', 'yo', 'tu tu', 'que', 'estas']
    twc = twitter_word_count(None)
    twc.get_last_week_tweets = MagicMock(return_value=tweets)
    assert twc.get_most_used_words_and_tweets() == []


def test_puntuation_marks():
    tweets = [',,,,', '....', '???', '!!!!', '¡¡¡¡¡', ';;;;', '::::::']
    twc = twitter_word_count(None)
    twc.get_last_week_tweets = MagicMock(return_value=tweets)
    assert twc.get_most_used_words_and_tweets() == []


def test_no_internet():
    twc = twitter_word_count(None)
    twc.get_last_week_tweets = MagicMock(
        side_effect=requests.exceptions.ConnectionError)  # Simulamos que no hay conexión a internet
    with pytest.raises(ValueError):
        twc.get_most_used_words_and_tweets()
