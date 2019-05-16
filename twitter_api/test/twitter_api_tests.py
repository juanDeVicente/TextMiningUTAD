import pytest
from unittest.mock import MagicMock

import requests

from twitter_api.src.twitter_api import twitter_api

def test_basic_spanish():
	tweets = ['hola', 'adios', 'hola adios', 'hola que tal']
	twc = twitter_api(None)
	twc.get_last_n_tweets = MagicMock(return_value=tweets)
	assert twc.get_last_week_tweets() == [['hola', 3, []]]