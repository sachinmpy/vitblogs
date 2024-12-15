from django.shortcuts import render
from blogs.models import Blog
from images_urls import get_random_image
# Typing imports
from django.http import HttpRequest
from django.shortcuts import HttpResponse

# TODO
# - Convert function based views to Class based views
# - Proper Annotation and type hinting


def homepage(request: HttpRequest) -> HttpResponse:
    """
    Homepage of the website

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    _blogs = Blog.objects.filter(is_approved=True).exclude(is_archived=True)[:5]
    _urls = [get_random_image() for i in range(5)]
    context: dict = {"blogs": _blogs, "image_func": get_random_image}

    return render(request, "sitepages/home.html", context=context)


# Note: This will be implemented later if needed, right now it does nothing
def aboutpage(request):  # MISSING: documentation, function annotation
    pass
