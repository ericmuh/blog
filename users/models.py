from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# Custom User Model
class CustomUser(AbstractUser):
    # Add any additional fields here
    age = models.IntegerField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
