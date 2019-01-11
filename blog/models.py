# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

BLOG_CATEGORIES = (
    ('Travel', 'TRAVEL'),
    ('LYH', 'LYH')
)

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=6, choices=BLOG_CATEGORIES, default='Lyh')
    created_date = models.DateTimeField(default = datetime.datetime.now())
    published_date = models.DateTimeField(blank=True, null=True)
    bg_image_skinny = models.ImageField(upload_to = 'images/')
    bg_image_wide = models.ImageField(upload_to = 'images/')
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def gettitle(self):
        return self.title
    
class PostImage(models.Model):
    blog_title = models.CharField(max_length=200, help_text='This field is for image storage. Try to keep this the same for all images for one blog and different for different blogs.', default='blogpost')
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    caption = models.TextField(default=None, blank=True, null=True)
    
    def gettitle(self):
        return self.post.title