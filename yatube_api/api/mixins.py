from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CreateUpdateDestroyForOwnerMixin:
    """
    Mixin what realize methods for object create, update, destroy.
    Update, destroy available only for Owner object.
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

    def update(self, request, pk=None, *args, **kwargs):
        obj = self.get_serializer_object(pk=pk, request=request)
        if obj.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, post_id=None, pk=None, *args, **kwargs):
        obj = self.get_serializer_object(pk=pk, request=request)
        if obj.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_object(self, pk, request):
        model = self.get_serializer().Meta.model
        return get_object_or_404(model, id=pk)
