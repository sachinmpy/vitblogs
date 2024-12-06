from django.shortcuts import render, redirect
from .models import Category, CategoryList
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Typing imports
from django.http import HttpRequest
from django.shortcuts import HttpResponse

# TODO
# - Convert function based views to Class based views
# - Proper Annotation and type hinting


def categories(request: HttpRequest) -> HttpResponse:
    """ """

    _categories = Category.objects.all()

    context: dict = {"categories": _categories}

    return render(request, "categories/categorypage.html", context=context)


def category_page(request: HttpRequest, category_name: str) -> HttpResponse:
    """ """
    try:
        _c = Category.objects.get(category=category_name)

    except ObjectDoesNotExist as e:
        messages.error(request, message=f"{category_name} does not exist")
        return redirect("/")

    category_list = CategoryList.objects.filter(category_name=_c)

    context: dict = {"cateogry": _c, "category_list": category_list}

    return render(request, "categories/categorylistpage.html", context=context)
