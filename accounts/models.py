from django.contrib.auth.models import AbstractUser
from django.db import models
from .forms import CustomUserManager


class CustomUser(AbstractUser):
    objects = CustomUserManager()


class Meta:
    swappable = 'AUTH_USER_MODEL'


# Specify related_name for groups and user_permissions fields
CustomUser._meta.get_field(
    'groups').remote_field.related_name = 'customuser_set'
CustomUser._meta.get_field(
    'user_permissions').remote_field.related_name = 'customuser_set'
