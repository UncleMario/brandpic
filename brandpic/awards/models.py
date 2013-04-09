from django.db import models

class Award(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=1024)

	def __unicode__(self):
		return u'%s' % (self.title)