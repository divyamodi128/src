from django.shortcuts import render
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver
from rest_framework import viewsets, permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.views import APIView
from rest_framework.response import Response

from collections import OrderedDict

from .serializers import CommentSerializers, CommentListSerializers
from .models import Comment


class CommentsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # lookup_field = 'id'


class ModelCommentsList(APIView):
    """
    List all Comments for corresponding Model.
    """
    # queryset = Comments.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, pk=None, format=None):
        comments = Comment.objects.filter(custom_model=pk)
        serializer = CommentListSerializers(
            comments, 
            context={'request': request},
            many=True
        )
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CommentSerializers(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomeCommentView(viewsets.ViewSet):
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return Comment.objects.all()

    def list(self, request):
        comments = self.get_queryset()
        serializer = CommentListSerializers(
            comments, 
            context={'request': request},
            many=True
        )
        # import pdb; pdb.set_trace()
        content = []
        for index, data in enumerate(serializer.data):
            if not data.get('parent_comment'):
                content.append(data)
                # serializer.data.pop(i)
            else:
                for cmt in content:
                    if cmt.get('url') == data.get('parent_comment'):
                        if cmt.get('reply'):
                            cmt.get('reply').append(data)
                            print(cmt)
                        else:
                            cmt['reply'] = [data,]
                        # serializer.data.pop(index)
                        # serializer.data.remove(data)
        return Response(content)

    def create(self, request):
        comment = Comment.objects.get()
        serializer = CommentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            comment(serializer.data)
            comment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

