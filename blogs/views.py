from django.shortcuts import render

# Typing imports
from django.http import HttpRequest
from django.shortcuts import HttpResponse

# TODO
# - Convert function based views to Class based views
# - Add Likes and Dislike functionality
# - Add Image upload, or make handling images seamless


def blog_page(request: HttpRequest) -> HttpResponse:
    """
    Page dedicated to show all the blogs posted in recent times
    this is second most important page in entire website


    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    context: dict = {}

    return render(request, "blogs/allblogs.html", context=context)


def blog(request: HttpRequest, blog_id: str) -> HttpResponse:  # Not working
    """
    Actual Blog which is written by users of the site,
    it takes blog_id to find the page in database

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    blog_id : str
        unique ID of blog to find blog in website

    Returns
    -------
    HttpResponse
        a HTML file
    """

    context: dict = {}

    return render(request, "blogs/blog.html", context=context)


def create_blog(request: HttpRequest) -> HttpResponse:  # Not working
    """
    this function will send webpage to user where they can create their blogs

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    context: dict = {}

    return render(request, "blogs/createblog.html", context=context)


def unverifed_blogs(request: HttpRequest) -> HttpResponse:  # Not working
    """
    list and displays all the unverified blogs

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    context: dict = {}

    return render(request, "blogs/unverifiedblogs.html", context=context)


def verify_blog(request: HttpRequest) -> HttpResponse:  # Not working
    """
    function that will verify blog into a verifed blog

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    context: dict = {}

    return render(
        request, "blogs/unverifiedblogs.html", context=context
    )
