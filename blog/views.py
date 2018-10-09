# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from .forms import ContactForm
from .models import Post


import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.

def post_list(request):
    posts = Post.objects.filter().order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def travel_list(request):
    posts = Post.objects.filter(category="Travel").order_by('-published_date')
    return render(request, 'blog/travel.html', {'posts': posts})

def lyh_list(request):
    posts = Post.objects.filter(category="LYH").order_by('-published_date')
    return render(request, 'blog/lyh.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/indiv_blog.html', {'post': post})

