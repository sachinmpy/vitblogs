from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# typing imports
from django.http import HttpRequest


def redirect_authenticated(view_function: callable) -> callable:
    """
    redirects users to home page who are already logged in to the site
    """

    def wrapper_func(request: HttpRequest, *args, **kwargs) -> callable:
        if request.user.is_authenticated:
            messages.warning(request, message="You are already Logged in?")
            return redirect("/")

        else:
            return view_function(request, *args, **kwargs)

    return wrapper_func


def redirect_non_staff(view_function: callable) -> callable:
    """
    redirects all users to home page which does not have site staff privilages
    """

    def wrapper_func(request: HttpRequest, *args, **kwargs) -> callable:
        if request.user.is_staff:
            messages.warning(request, message="NOT PERMITTED!")
            return view_function(request, *args, **kwargs)

        else:
            return redirect("/")

    return wrapper_func


def redirect_unknown_user(view_function: callable) -> callable:
    """ """

    def wrapper_func(request: HttpRequest, username: str, *args, **kwargs) -> callable:
        try:
            _user = User.objects.get(username=username)

        except ObjectDoesNotExist as e:
            messages.error(request, message="Does not exist")
            return redirect("/")

        return view_function(request, username)

    return wrapper_func
