# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Post
import sendgrid
from sendgrid.helpers.mail import *


import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.

def post_list(request):
    posts = Post.objects.filter().order_by('-published_date').all()[:11]
    
    newposts = organizePosts(posts);
    bigs = [5,9]
    smalls = [1,2,3,4,6,7,8,10]
    
    return render(request, 'blog/index.html', {'posts': newposts, 'bigs' : bigs, 'smalls' : smalls})

def travel_list(request):
    posts = Post.objects.filter(category="Travel").order_by('-published_date')
    
    newposts = organizePosts(posts);
    bigs, smalls = createBigSmall(len(newposts))
    
    return render(request, 'blog/travel.html', {'posts': newposts, 'bigs' : bigs, 'smalls' : smalls})

def lyh_list(request):
    posts = Post.objects.filter(category="LYH").order_by('-published_date')
    
    newposts = organizePosts(posts);
    bigs, smalls = createBigSmall(len(newposts))
    
    return render(request, 'blog/lyh.html', {'posts': newposts, 'bigs' : bigs, 'smalls' : smalls})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/indiv_blog.html', {'post': post})

def organizePosts(posts):
    newposts = []
    
    counter = 0
    for p in posts:
        post = {
            'thispost' : p,
            'index' : counter
        }
        newposts.append(post)
        counter += 1
    return newposts

def createBigSmall(length):
    bigs = []
    smalls = []
    
    counter = 0
    while counter < length:
        bigs.append(counter)
        if len(bigs) % 2 != 0:
            counter += 6
        else:
            counter += 4
    
    counter = 0
    while counter < length:
        if counter not in bigs:
            smalls.append(counter)
        counter += 1
        
    return bigs, smalls

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                sg = sendgrid.SendGridAPIClient('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')
                from_email = Email(from_email)
                to_email = Email("gage_payne37@yahoo.com")
                subject = subject
                content = Content("text/plain", message)
                mail = Mail(from_email, subject, to_email, content)
                response = sg.client.mail.send.post(request_body=mail.get())
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "blog/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')