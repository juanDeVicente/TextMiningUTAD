from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('frequency', views.search_frequency_words, name='frequency')
]
