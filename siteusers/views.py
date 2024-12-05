from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, UserProfile
from .forms import UserCreationForm, UserProfileForm, UserLoginForm
from decorators import redirect_authenticated  # Redirects already logged in users 

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

    
    return redirect('/')

@redirect_authenticated
def registeruser(request: HttpRequest) -> HttpResponse:
    pass


@login_required
def user_profile(request: HttpRequest, username: str) -> HttpResponse:
    pass


@login_required
def user_profile_setting(request: HttpRequest, username: str) -> HttpResponse:
    pass


@login_required
def user_blogs(request: HttpRequest, username: str) -> HttpResponse:
    pass


def verify_user_email():
    pass
