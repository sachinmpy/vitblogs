"""
URL configuration for vitblogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('blogs', blog_page, name='blog_page'),
    path('blogs/blog/<str:id>', blog, name='blog'),
    path('blogs/create-blog', create_blog, name='create_blog'),
    path('blogs/unverified-blogs', unverifed_blogs, name='unverified_blogs'),
    path('blogs/verify-blog', verify_blog, name='verify_blog'),
]
