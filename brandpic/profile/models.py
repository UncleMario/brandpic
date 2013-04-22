from django.contrib.auth.models import User 
from django.db import models
from django.db.models.signals import post_save

from django_facebook.models import FacebookProfileModel
from tastypie.models import create_api_key

from brandpic.brands.models import Brand
from brandpic.awards.models import Award


class Profile(FacebookProfileModel):
	user = models.OneToOneField(User)
	brands = models.ManyToManyField(Brand)
	awards = models.ManyToManyField(Award)

	def __unicode__(self):
		return u'%s' % (self.user)

	#Create profile when new user
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	#Signal to create user profile
	post_save.connect(create_user_profile, sender=User)
	#Signal to create apy key to tastypie
	post_save.connect(create_api_key, sender=User)
