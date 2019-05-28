from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .forms import search_form
from twitter_api.src.twitter_api import twitter_word_count


def index(request):
	'''
	Return index page, the form
	:param request:
	:return: the index.html page
	'''
	return render(request, 'index.html', {'search_form': search_form})


def search_frequency_words(request):
	if request.method == 'POST' and request.is_ajax():
		form = search_form(request.POST)
		if form.is_valid():
			screen_name = form.cleaned_data['screen_name']
			language = form.cleaned_data['language']
			frequency_words = twitter_word_count(settings.API_TWITTER).get_most_used_words_and_tweets(screen_name, language)
			if len(frequency_words) == 0:
				return HttpResponse('No hay tweets disponibles')
			return render(request, 'tweets_list.html', {'frequency_words': frequency_words})
		response = HttpResponse('El formulario no es valido')
		response.status_code = 400

		return response
	response = HttpResponse('Petición no válida')
	response.status_code = 400
	return response
