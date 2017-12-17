# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100, default= '')
	city = models.CharField(max_length = 100, default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default = 0)
	
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender = User)

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class WebsitePost(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author)

class AssignmentPost(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author)
        
class SurvivingPost(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author)

class LectureSlidesPost(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author)
        
class ChartsPost(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author)
        
class BinaryPost(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=64)
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author)
