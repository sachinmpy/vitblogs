from django.shortcuts import redirect

# typing imports
from django.http import HttpRequest


def redirect_authenticated(view_function: callable) -> callable:

    def wrapper_func(request: HttpRequest, *args, **kwargs) -> callable:
        if request.user.is_authenticated:
            return redirect("/")

        else:
            return view_function(request, *args, **kwargs)

    return wrapper_func
