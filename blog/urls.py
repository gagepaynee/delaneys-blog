from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('travel/', views.travel_list, name="travel_list"),
    path('lyh/', views.lyh_list, name="lyh_list"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
]