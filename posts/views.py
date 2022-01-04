# Django
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework.viewsets import ModelViewSet

# Local Models
from posts.models import Post
from posts.serializers import PostSerializer
from posts.permissions import IsAdminOrReadOnlyPermission

class PostViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnlyPermission]
  serializer_class = PostSerializer
  queryset = Post.objects.filter(published=True)
  lookup_field = 'slug'
  filter_backends = [DjangoFilterBackend]
  # filterset_fields = ['category']
  filterset_fields = ['category__slug']