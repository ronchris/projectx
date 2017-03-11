from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Destination(models.Model):
	name = models.CharField(max_length=255)
	municipality = models.CharField(max_length=255)
	province = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	description = models.TextField()
	features = models.TextField()
	activities = models.TextField()
	misc = models.TextField()
	slug = models.SlugField(unique=True)
	user = models.OneToOneField(User, blank=True, null=True)