#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clase que permite contar las palabras de los útlimos tweets
"""
import requests

from word_frequency.src import word_frequency
from functools import reduce
from datetime import datetime, timedelta

import twitter
import os

ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''


class twitter_word_count(object):

	def __init__(self, api):
		self.api = api

	def get_last_week_tweets(self, screen_name=None):

		last_week = datetime.today() - timedelta(days=7)
		return [x.full_text
				for x in
				self.api.GetUserTimeline(screen_name=screen_name, count=200, include_rts=False, exclude_replies=False)
				if datetime.strptime(x.created_at, '%a %b %d %H:%M:%S %z %Y').timestamp() > last_week.timestamp()
				]

	def get_most_used_words_and_tweets(self, screen_name=None, language='spanish'):
		try:
			tweets = self.get_last_week_tweets(screen_name)
		except requests.exceptions.ConnectionError:
			raise ValueError('No hay conexion a Internet')

		if tweets is []:
			return []

		tweets_array = reduce((lambda x, y: x + ', ' + y), tweets)
		counted_words = word_frequency.word_frequency(tweets_array, language)[0:10]
		return self.create_words_and_tweets_matrix(tweets, counted_words)

	def create_words_and_tweets_matrix(self, tweets, words):
		matrix = []
		aux_tweet_list = []
		for key, timesUsed in words:
			for tweet in tweets:
				aux_lowercase_tweet = tweet.lower()

				if key in aux_lowercase_tweet:
					aux_tweet_list.append(tweet)
			matrix.append([key, timesUsed, aux_tweet_list])
			aux_tweet_list = []

		return matrix


if __name__ == "__main__":
	try:
		ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
		ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
		CONSUMER_KEY = os.environ['CONSUMER_KEY']
		CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
	except KeyError:
		print('No se ha establecido algun parametro para conectar con la api de Twitter')
		exit(-1)

	print('ACCESS_TOKEN_KEY:', ACCESS_TOKEN_KEY)
	print('ACCESS_TOKEN_SECRET:', ACCESS_TOKEN_SECRET)
	print('CONSUMER_KEY:', CONSUMER_KEY)
	print('CONSUMER_SECRET:', CONSUMER_SECRET)

	api = twitter.Api(
		CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, tweet_mode='extended'
	)
	screen_name = 'realdonaldtrump'  # Aqui va le nombre de la cuenta que queramos mirar (Arturo Perez Reverte) Si es None, devuelve los del usuario a los que este asociado la cuenta

	language = 'english'
	twc = twitter_word_count(api)

	for x in twc.get_most_used_words_and_tweets(screen_name, language):
		print(x)
