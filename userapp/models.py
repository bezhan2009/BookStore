from django.db import models
from django.contrib.auth.models import User


class UserProfile(User):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
