# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Local Models
from comments.views import CommentApiViewSet

router_comments = DefaultRouter()

router_comments.register(prefix='comments', basename='comments', viewset=CommentApiViewSet)