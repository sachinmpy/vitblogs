from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Seperate user profile from django base User class
    idea is to have different way to store settings decoupled from actual user account
    """

    # Choices Classes
    class CourseChoices(models.TextChoices):
        DEFAULT = "--", "--------"

    class DegreeChoices(models.TextChoices):
        DEFAULT = "--", "--------"

    class DesignationChoices(models.TextChoices):
        DEFAULT = "--", "--------"
        STUDENT = "ST", "Student"
        STAFF = "SF", "Staff"
        ALUMNI = "AL", "Alumni"

    # model attributes definition
    about_me = models.TextField(max_length=250, default="")
    belongs_to = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(
        max_length=2, choices=CourseChoices, default=CourseChoices.DEFAULT
    )
    degree = models.CharField(
        max_length=2, choices=DegreeChoices, default=DegreeChoices.DEFAULT
    )
    designation = models.CharField(
        max_length=2, choices=DesignationChoices, default=DegreeChoices.DEFAULT
    )
    university_joined_date = models.DateField(null=True)

    def __str__(self):
        return self.belongs_to.username


@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created: bool, **kwargs) -> None:
    """
    creates seperate empty user profile soon after creation of user

    Parameter
    ---------
    sender
        base User model in django

    instance
        actual instance being saved

    created : bool
        True if new record is created

    Returns
    ------
    None
    """
    if created:
        UserProfile.objects.create(belongs_to=instance)
