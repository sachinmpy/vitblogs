from django.db import models
from blogs.models import Blog
# Create your models here.

class Category(models.Model):
    """
    """

    category = models.CharField(max_length=32, null=False, unique=True)

    def __str__(self):
        return f"{self.category}"


class CategoryList(models.Model):
    """
    """

    category_name = models.ForeignKey(Category, related_name="category_name", on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name="id", on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.category_name}->{self.blog_id}"