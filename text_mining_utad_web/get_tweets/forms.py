from django import forms
from nltk.corpus import stopwords


class search_form(forms.Form):
	screen_name = forms.CharField(label='Your name', max_length=100)
	screen_name.widget.attrs.update({'placeholder': 'screen_name', 'class': 'form-control'})

	language = forms.ChoiceField(choices=[(x, x.capitalize()) for x in stopwords.fileids()])
	language.widget.attrs.update({'class': 'form-control'})

