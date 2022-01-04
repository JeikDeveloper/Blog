# Django Rest Framework
from rest_framework import serializers

# Local Models
from posts.models import Post
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  category = CategorySerializer()

  class Meta:
    model = Post
    fields = [
      'title', 'content', 'slug',
      'miniature', 'created_at', 'published',
      'user', 'category'
    ]