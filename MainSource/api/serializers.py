from rest_framework import serializers
from MainSource.models import Author, Publisher, Genre, Category, Discount, Inventory, Book, ShoppingCart, Order, Review
from userapp.models import UserProfile


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'name', 'discount_percentage']


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'quantity']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'published_date', 'author', 'publisher', 'genre', 'category', 'discount', 'inventory', 'price', 'cover_image']


class ShoppingCartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all(),
        required=False
    )

    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'book', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all(),
        required=False
    )

    class Meta:
        model = Order
        fields = ['id', 'user', 'books', 'date_ordered', 'authorized']


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=UserProfile.objects.all(),
        required=False
    )

    class Meta:
        model = Review
        fields = ['id', 'user', 'book', 'rating', 'comment', 'date_added', 'approved']
