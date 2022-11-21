"""
module for authentication models
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager



class User(AbstractUser):
    """
    custom user model
    """
    username = None
    first_name = None
    last_name = None
    email = models.EmailField('email address', unique=True)
    phone = models.CharField(max_length=3086, blank=True)
    name = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email