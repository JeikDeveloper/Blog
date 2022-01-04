# Django
from django.contrib import admin

# Local Model
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['content', 'user', 'post', 'created_at']