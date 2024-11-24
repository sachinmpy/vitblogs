import uuid
import datetime
from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """
    Blog model will emulate behaviour of blog written by User
    """

    approved_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name="approved_by",
    )
    banner_link = models.URLField(max_length=256, null=True, blank=True, default=None)
    blog_id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    content = models.TextField(null=False)
    create_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=False)
    headline = models.CharField(max_length=70, null=False)
    is_approved = models.BooleanField(default=False)
    short_description = models.TextField(max_length=50, null=False)

    def __str__(self):
        return f"{self.headline[:15]} by: {self.blog_id}"
