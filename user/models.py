from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager

__all__ = ["User"]


class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return f"{self.username}"
