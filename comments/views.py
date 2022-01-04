# Django
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

# Local Models
from comments.models import Comment
from comments.serializers import CommentSerializer
from comments.permissions import IsOwnerOrReadAndCreateOnly

class CommentApiViewSet(ModelViewSet):
  #permission_classes = [IsOwnerOrReadAndCreateOnly]
  permission_classes = [IsOwnerOrReadAndCreateOnly]
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()
  filter_backends = [OrderingFilter, DjangoFilterBackend]
  ordering = ['-created_at']
  filterset_fields = ['post']