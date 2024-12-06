from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import User, UserProfile
from blogs.models import Blog
from .forms import UserCreationForm, UserProfileForm, UserLoginForm
from decorators import redirect_authenticated, redirect_unknown_user

# Typing Imports
from django.http import HttpResponse, HttpRequest

# TODO
# - Convert function based views to Class based views
# - Verify user email through inbox emails


@redirect_authenticated
def loginuser(request: HttpRequest) -> HttpResponse:
    """
    Login page

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    form = UserLoginForm()

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        # proceed to login if user is authenticated
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}")
            return redirect("/")

        # sends error if not able to login
        messages.error(request, "username or password is wrong")

    context: dict = {"form": form}
    return render(request, "siteusers/login.html", context=context)


@login_required(login_url="loginuser")
def logoutuser(request: HttpRequest) -> HttpResponse:
    """
    Logout, it will not render any page but is a standalone function

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """

    logout(request)
    messages.success(request, message="User was logged out successfully")
    return redirect("/")


@redirect_authenticated
def registeruser(request: HttpRequest) -> HttpResponse:
    """
    Register user

    Parameters
    ----------
    request : HttpRequest
        request captures http request response sent via urls

    Returns
    -------
    HttpResponse
        a HTML file
    """
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            pass  # IMPLEMENT THIS FUTURE ME

    context: dict = {
        "form": form,
    }

    return render(request, "siteusers/register.html", context=context)


@login_required(login_url="loginuser")
@redirect_unknown_user
def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    """ """
    _u = User.objects.get(username=username)
    user_blogs = Blog.objects.filter(create_by=_u)

    context: dict = {"user": _u, "user_blogs": user_blogs}
    return render(request, "siteusers/userprofile.html")


# IMPLEMENT THIS FUTURE ME
@login_required(login_url="loginuser")
@redirect_unknown_user
def user_profile_setting(request: HttpRequest, username: str) -> HttpResponse:
    """ """
    _u = User.objects.get(username=username)
    context: dict = {"user": _u}
    return render(request, "siteusers/profilesettings.html", context=context)


def verify_user_email():
    pass
