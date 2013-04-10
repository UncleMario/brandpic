from django import forms
from django.forms import ModelForm, Textarea

from brandpic.pictures.models import Picture


class PictureForm(ModelForm):
	class Meta:
		model = Picture
		exclude = ('owner','brands','awards','date',)
		widgets = {
			'description' : Textarea(attrs={'class':'span10'})
		}