from rest_framework.response import Response
from rest_framework import status


class CustomCreateMixin:
    """
    Add create method what set autor as request.user.
    If has post_id, add post_id.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        post_id = kwargs.get('post_id')
        if serializer.is_valid():
            if post_id:
                serializer.save(author=request.user, post_id=post_id)
            else:
                serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
