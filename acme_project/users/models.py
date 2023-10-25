from django.db import models

# users/models.py
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    bio = models.TextField('Биография', blank=True)