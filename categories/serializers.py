# Django Rest Framework
from rest_framework import serializers

# Local Models
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'title', 'slug', 'published']
