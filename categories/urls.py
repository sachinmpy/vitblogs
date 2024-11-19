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
    path('categories/list', categories, name='categories'),
    path('categories/category/<id:str>', category_page, name='category_page'),
    path('categories/create_category', create_category, name='create_category'),
]
