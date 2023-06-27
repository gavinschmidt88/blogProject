from django.contrib.auth.models import AbstractUser
from .forms import CustomUserManager
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField()
    location = models.CharField(max_length=255)

    # You can add more custom fields here

    def __str__(self):
        return self.username


class Meta:
    swappable = 'AUTH_USER_MODEL'


# Specify related_name for groups and user_permissions fields
CustomUser._meta.get_field(
    'groups').remote_field.related_name = 'customuser_set'
CustomUser._meta.get_field(
    'user_permissions').remote_field.related_name = 'customuser_set'
