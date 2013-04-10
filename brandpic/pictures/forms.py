from django import forms
from django.forms import ModelForm

from brandpic.pictures.models import Picture


class PictureForm(ModelForm):
	class Meta:
		model = Picture
		exclude = ('owner','awards','date',)