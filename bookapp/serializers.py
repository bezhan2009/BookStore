from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'published_date', 'author', 'publisher', 'genre', 'category', 'discount', 'inventory', 'price', 'cover_image']
