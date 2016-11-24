from __future__ import unicode_literals

from django.db import models

class Travel(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	siteurl = models.CharField(max_length=255, blank=True)
	image = models.ImageField(blank=True)
	image2 = models.ImageField(blank=True)
	image3 = models.ImageField(blank=True)
	image4 = models.ImageField(blank=True)
	logo = models.ImageField(blank=True)
	dias = models.CharField(max_length=255,blank=True)
	includes = models.CharField(max_length=500, blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

