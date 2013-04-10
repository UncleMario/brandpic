from django import forms
from django.forms import ModelForm, Textarea, ClearableFileInput
from brandpic.pictures.models import Picture


class PictureForm(ModelForm):
	class Meta:
		model = Picture
		exclude = ('owner','brands','awards','date',)
		widgets = {
			'picture': ClearableFileInput(attrs={'id':'file-uploader-input','class':'file'}),
			'description' : Textarea(attrs={'rows':'5'}),
		}