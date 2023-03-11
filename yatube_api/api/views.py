from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from .mixins import CustomCreateMixin
from .permissions import OwnerOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(CustomCreateMixin, viewsets.ModelViewSet):
    """
    ViewSet for Post.
    Permission for authorized: GET, POST.
    Permission for authors - PUT, PATCH, DELETE.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated & OwnerOrReadOnly]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Group.
    Permission for authorized: GET.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(CustomCreateMixin, viewsets.ModelViewSet):
    """
    ViewSet for Comment.
    Permission for authorized: GET, POST.
    Permission for authors - PUT, PATCH, DELETE.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated & OwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()
