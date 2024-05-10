from django.db import models
from django.contrib.auth.models import User
from bookapp.models import Book


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    parent_id = models.IntegerField(null=True)
    comment_text = models.TextField()
