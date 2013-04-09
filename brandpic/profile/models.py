from django.contrib.auth.models import User 
from django.db import models
from django.db.models.signals import post_save

from django_facebook.models import FacebookProfileModel

from brandpic.brands.models import Brand


class Profile(FacebookProfileModel):
	user = models.OneToOneField(User)
	brands = models.ManyToManyField(Brand)

	def __unicode__(self):
		return u'%s' % (self.user)

	#Create profile when new user
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	post_save.connect(create_user_profile, sender=User)
