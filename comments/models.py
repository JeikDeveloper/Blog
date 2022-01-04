# Django
from django.db import models
from django.db.models import CASCADE

# Local Models
from users.models import User
from posts.models import Post

class Comment(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=CASCADE, null=True)
  post = models.ForeignKey(Post, on_delete=CASCADE, null=True)