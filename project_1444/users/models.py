from django.db import models

from django.contrib.auth.models import AbstractUser


# Таблиця користувачів
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    bithday = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


    
    def __str__(self):
        return self.name

