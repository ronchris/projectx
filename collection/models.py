from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from registration.signals import user_registered
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import AbstractUser
import numpy as np

	
class Province(models.Model):
	name = models.CharField(max_length=255)
	author = models.CharField(max_length=255, blank=True, null=True)
	kind = models.CharField(max_length=255)
	address = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField()
	coords = models.CharField(max_length=255, blank=True, null=True)
	slug = models.SlugField(unique=True)
	image = models.ImageField(blank=True, null=True)
	
	def __str__(self):
		return self.name
	
class Muni(models.Model):
	name = models.CharField(max_length=255)
	author = models.CharField(max_length=255, blank=True, null=True)
	kind = models.CharField(max_length=255)
	province = models.ForeignKey(Province, on_delete=models.CASCADE)
	address = models.CharField(max_length=255, blank=True, null=True)
	accessibility = models.CharField(max_length=255, blank=True, null=True)
	description = models.TextField()
	safety_rating = models.CharField(max_length=255, blank=True, null=True)
	population = models.CharField(max_length=255, blank=True, null=True)
	known_for = models.CharField(max_length=255, blank=True, null=True)
	misc = models.TextField(blank=True, null=True)
	activities = models.TextField(blank=True, null=True)
	features = models.TextField(blank=True, null=True)
	coords = models.CharField(max_length=255, blank=True, null=True)
	slug = models.SlugField(unique=True)
	image = models.ImageField(blank=True, null=True)
	
	def __str__(self):
		return self.name

class Destination(models.Model):
	name = models.CharField(max_length=255)
	author = models.CharField(max_length=255, blank=True, null=True)
	kind = models.CharField(max_length=255)
	muni = models.ForeignKey(Muni, on_delete=models.CASCADE)
	province = models.ForeignKey(Province, on_delete=models.CASCADE)
	address = models.CharField(max_length=255)
	description = models.TextField()
	features = models.TextField()
	activities = models.TextField()
	misc = models.TextField()
	coords = models.TextField()
	slug = models.SlugField(unique=True)
	image = models.ImageField()
	user = models.OneToOneField(User, blank=True, null=True)
	saves = models.IntegerField(default=0)
	savers = models.ManyToManyField(User, related_name="savers")
	
	def get_savers(self):
		saver_list = []
		for saver in self.savers.all():
			#print 'saver',saver
			saver_list.append(saver.username)
		return saver_list
	
	
	def average_rating(self):
		all_ratings = map(lambda x: x.rating, self.review_set.all())
		return np.mean(all_ratings)
	
	def __str__(self):
		return self.name + ' - ' + self.address

def get_image_path(instance, filename):
	return '/'.join(['destination_images', instance.destination.slug, filename])

class Upload(models.Model):
	destination = models.ForeignKey(Destination, related_name="uploads")
	image = models.ImageField(upload_to=get_image_path)

class Review(models.Model):
	RATING_CHOICES = (
		(0,'0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
	destination = models.ForeignKey(Destination)
	pub_date = models.DateTimeField('date published')
	user_name = models.ForeignKey(User)
	comment = models.TextField(blank=False)
	rating = models.IntegerField(choices=RATING_CHOICES, blank=False)
	likes = models.IntegerField(default=0)
	likers = models.ManyToManyField(User, related_name="likers")
	
	def get_likers(self):
		liker_list = []
		for liker in self.likers.all():
			#print 'liker',liker
			liker_list.append(liker.username)
		return liker_list
	
	
class Question(models.Model):
	destination = models.ForeignKey(Destination)
	pub_date = models.DateTimeField('date published')
	user_name = models.ForeignKey(User)
	message = models.TextField(blank=False)	
	
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	review = models.ForeignKey(Review, null=True, blank=True)
	question = models.ForeignKey(Question, null=True, blank=True)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	image = models.ImageField(null=True, blank=True)
	
class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	review = models.ForeignKey(Review, related_name="reviews")
	author = models.CharField(max_length=200, null=True, blank=True)
	text = models.TextField(null=True, blank=True)
	created_date = models.DateTimeField('date published')
	
class CommentQ(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, related_name="questions")
	author = models.CharField(max_length=200, null=True, blank=True)
	text = models.TextField(null=True, blank=True)
	created_date = models.DateTimeField('date published')
	
def create_user_profile(sender, user, request, **kwargs):
	print "create_user_profile"
	Profile.objects.create(user=user)
user_registered.connect(create_user_profile)
