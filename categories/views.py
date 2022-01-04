# Django
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Django Rest Framework
from rest_framework.viewsets import ModelViewSet

# Local Models
from categories.models import Category
from categories.serializers import CategorySerializer
from categories.permissions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
  permission_classes = [IsAdminOrReadOnly]
  serializer_class = CategorySerializer
  # queryset = Category.objects.all()
  queryset = Category.objects.filter(published=True)
  lookup_field = 'slug'
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['title']