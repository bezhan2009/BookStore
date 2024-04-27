from django.db import models
from django.contrib.auth.models import User
from userapp.models import UserProfile
from bookapp.models import (Book,
                            Genre,
                            Discount,
                            Category,
                            Inventory,
                            Author,
                            Publisher,
                            )


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
    date_ordered = models.DateTimeField(auto_now_add=True)
    authorized = models.BooleanField(default=False)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
