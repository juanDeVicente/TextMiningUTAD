import pytest
from unittest.mock import MagicMock

import requests



#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from unittest.mock import MagicMock

import requests

from twitter_api.src.twitter_word_count import *

from twitter_api.src.twitter_api import twitter_word_count


def test_example():
    tweets = ['hola', 'que tal estas', 'pues yo muy bien']
    twc = twitter_word_count(None)
    twc.get_last_week_tweets = MagicMock(return_value=tweets)
    assert twc.get_most_used_words_and_tweets() == [('hola', 1), ('tal', 1), ('pues', 1), ('bien', 1)]


def test_quijote():
    tweets = ['En un lugar de la Mancha, de cuyo nombre no quiero acordarme,',
              'o ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,', 'adarga antigua, rocín flaco',
              ' y galgo corredor', 'Una olla de algo más vaca que carnero, ',
              'salpicón las más noches, duelos y quebrantos los sábados,', 'sábados', 'y lentejas los viernes']
    twc = twitter_word_count(None)
    twc.get_last_week_tweets = MagicMock(return_value=tweets)
    print(twc.get_words_of_tweets())
    assert twc.get_most_used_words_and_tweets() == [['sábados', 9.52,[ 'salpicón las más noches, duelos y quebrantos los sábados,',
																	   'sábados']],
													['lugar', 4.76,['En un lugar de la Mancha, de cuyo nombre no quiero acordarme,']],
													['mancha', 4.76,['En un lugar de la Mancha, de cuyo nombre no quiero acordarme,']],
													['cuyo', 4.76,['En un lugar de la Mancha, de cuyo nombre no quiero acordarme,']],
													['nombre', 4.76,['En un lugar de la Mancha, de cuyo nombre no quiero acordarme,']],
													['quiero', 4.76,['En un lugar de la Mancha, de cuyo nombre no quiero acordarme,']],
													['acorda1rme', 4.76,['En un lugar de la Mancha, de cuyo nombre no quiero acordarme,']],
													['tiempo', 4.76,['o ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,']],
													['vivía', 4.76,['o ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,']],
													['hidalgo', 4.76,['o ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,']],
													['lanza', 4.76,['o ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,']]
													]

'''
													['astillero', 4.76,['o ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,']],
													['adarga', 4.76,['adarga antigua, rocín flaco']], 
													['antigua', 4.76,['adarga antigua, rocín flaco']],
													['rocín', 4.76,['adarga antigua, rocín flaco']],
													['flaco', 4.76,['adarga antigua, rocín flaco']],
													['galgo', 4.76,[' y galgo corredor']],
													['corredor', 4.76,[' y galgo corredor']],
													['olla', 4.76],
													['vaca', 4.76]]
'''


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