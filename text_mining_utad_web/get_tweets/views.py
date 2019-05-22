from django.shortcuts import render
from .forms import search_form


def index(request):
	return render(request, 'index.html', {'search_form': search_form})
