# Django Rest Framework
from rest_framework import serializers

# Local Models
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['content', 'created_at', 'user', 'post']