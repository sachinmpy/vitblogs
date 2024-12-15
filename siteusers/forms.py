from django import forms

from .models import User, UserProfile


class UserCreationForm(forms.ModelForm):
    """ """

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserProfileForm(forms.ModelForm):
    """ """

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserLoginForm(forms.ModelForm):
    """ """

    class Meta:
        model = User
        fields = ("username", "password")
