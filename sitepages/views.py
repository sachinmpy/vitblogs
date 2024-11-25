from django.shortcuts import render

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

    context: dict = {}

    return render(request, "sitepages/home.html", context=context)


# Note: This will be implemented later if needed, right now it does nothing
def aboutpage(request):  # MISSING: documentation, function annotation
    pass
