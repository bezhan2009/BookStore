from rest_framework import serializers
from .models import Comment
from userapp.models import UserProfile
from bookapp.models import Book


class CommentChildrenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    comment_text = serializers.CharField()
    parent_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ['id', 'comment_text', 'parent_id']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserProfile.objects.all(), required=False)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class CommentMainSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    comment_text = serializers.CharField()
    parent_id = serializers.IntegerField()
    children = CommentChildrenSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'comment_text', 'parent_id', 'children']
