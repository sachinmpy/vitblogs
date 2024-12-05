from django import forms
from .models import Blog


class BlogCreationForm(forms.Form):
    """
    """

    class Meta:
        model = Blog
        fields = "__all__"

