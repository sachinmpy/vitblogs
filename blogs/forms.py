from django import forms
from django.forms import ModelChoiceField
from .models import Blog
from categories.models import Category


class BlogCreationForm(forms.ModelForm):
    """ """

    category = ModelChoiceField(queryset=Category.objects.all(), empty_label="----")

    class Meta:
        model = Blog
        fields = "__all__"
