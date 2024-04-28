from django.db import models
from django.contrib.auth.models import User
from bookapp.models import Book


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    date_ordered = models.DateTimeField(auto_now_add=True)
    authorized = models.BooleanField(default=False)
