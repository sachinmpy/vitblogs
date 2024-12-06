from django import forms
from .models import User, UserProfile


class UserCreationForm(forms.Form):
    """ """

    class Meta:
        model = User
        fields = "__all__"


class UserProfileForm(forms.Form):
    """ """

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserLoginForm(forms.Form):
    """ """

    class Meta:
        model = User
        fields = ("username", "password")
