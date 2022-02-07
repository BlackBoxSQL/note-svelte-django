from django.db import models

# Create your models here.
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")

    USERNAME_FIELD = "username"  # e.g: "username", "email"
    EMAIL_FIELD = "email"  # e.g: "email", "primary_email"


class Note(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Notes"

    def __str__(self):
        return self.title
