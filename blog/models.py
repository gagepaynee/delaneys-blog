# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
from PIL import Image, ExifTags
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

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

@receiver(post_save, sender=PostImage, dispatch_uid="update_image_postimage")
def update_image(sender, instance, **kwargs):
    if instance.image:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fullpath = BASE_DIR + instance.image.url
        rotate_image(fullpath)

@receiver(post_save, sender=Post, dispatch_uid="update_image_post")
def update_image2(sender, instance, **kwargs):
    if instance.bg_image_skinny:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fullpath = BASE_DIR + instance.bg_image_skinny.url
        rotate_image(fullpath)
    if instance.bg_image_wide:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        fullpath = BASE_DIR + instance.bg_image_wide.url
        rotate_image(fullpath)

        
def rotate_image(filepath):
    try:
        image = Image.open(filepath)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(image._getexif().items())

        if exif[orientation] == 3:
            image = image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image = image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image = image.rotate(90, expand=True)
        image.save(filepath)
        image.close()
    except (AttributeError, KeyError, IndexError):
        pass