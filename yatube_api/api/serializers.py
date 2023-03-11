from django.contrib.auth import get_user_model
from rest_framework import serializers
from posts.models import Post, Group, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model."""
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model."""
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
