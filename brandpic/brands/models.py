from django.db import models

from brandpic.awards.models import Award

class Brand(models.Model):
	name = models.CharField(max_length=55)
	awards = models.ManyToManyField(Award)
	usage = models.IntegerField(default=0)

	def __unicode__(self):
		return u'%s' % (self.name)
