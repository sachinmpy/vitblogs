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
    path('users/login', loginuser, name='loginuser'),
    path('users/logout', logoutuser, name='logoutuser'),
    path('users/register', registeruser, name='register'),
    path('users/<str:username>/profile', user_profile, name='user_profile'),
    path('users/<str:username>/settings', user_profile_setting, name='user_profile_setting'),
    path('users/<str:username>/user-blogs', user_blogs, name='user_blogs'),
]
