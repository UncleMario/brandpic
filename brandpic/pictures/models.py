from django.db import models
from django.contrib.auth.models import User

from brandpic.brands.models import Brand
from brandpic.pictures.functions import make_upload_path
from brandpic.awards.models import Award

class Picture(models.Model):
	owner = models.ForeignKey(User)
	picture = models.ImageField(upload_to=make_upload_path)
	brands = models.ManyToManyField(Brand)
	description = models.CharField(max_length=360)
	awards = models.ManyToManyField(Award)
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.picture.url

	def get_url(self):
		return str(self.picture.url).split("?")[0]

