from rest_framework import viewsets
from posts.models import Comment, Group, Post
from .mixins import CreateUpdateDestroyForOwnerMixin
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(CreateUpdateDestroyForOwnerMixin, viewsets.ModelViewSet):
    """
    ViewSet for Post.
    Allows methods: GET, POST, PUT, PATCH, DELETE.
    PUT, PATCH, DELETE - available for authors.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Group.
    Allows methods: Get.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(CreateUpdateDestroyForOwnerMixin, viewsets.ModelViewSet):
    """
    ViewSet for Comment.
    Allows methods: GET, POST, PUT, PATCH, DELETE.
    PUT, PATCH, DELETE - available for authors.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return Comment.objects.filter(post=post_id)
