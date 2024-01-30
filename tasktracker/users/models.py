from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # using email instead of username
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
