from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Video(models.Model):
	title = models.CharField(max_length=150)
	url = models.CharField(max_length=150)
	main = models.BooleanField(default='false')

	def __unicode__(self):
		return self.title
