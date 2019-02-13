# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, PostImage

# Register your models here.

class PostImageAdmin(admin.ModelAdmin):
    pass

class PostImageInline(admin.StackedInline):
    model = PostImage
    max_num = 40
    extra = 0
    
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ['title']
    save_as = True
    

admin.register(PostImage, PostImageAdmin)
admin.site.register(Post, PostAdmin)