from django.db import models

from brandpic.awards.models import Award

class Brand(models.Model):
	name = models.CharField(max_length=55)
	awards = models.ManyToManyField(Award)
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % (self.name)
