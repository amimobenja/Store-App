from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	description = models.TextField()
	likes = models.IntegerField(default=0, null=True)
	image = models.ImageField(upload_to='category_images')
	
	def __unicode__(self):
		return self.name

class Item(models.Model):
	category =  models.ForeignKey(Category)
	item_name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	item_description = models.TextField()
	price = models.CharField(max_length=128, null=True)
	photos = models.ImageField(upload_to='item_images')
	address = models.TextField()
	shops_info = models.TextField()
	
	def __unicode__(self):
		return self.item_name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images')
	
	def __unicode__(self):
		return self.user.username
