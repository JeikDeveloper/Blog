# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Local Models
from posts.views import PostViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='posts', basename='posts', viewset=PostViewSet)
