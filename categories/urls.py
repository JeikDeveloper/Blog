# Django Rest Framework
from rest_framework.routers import DefaultRouter

# Local Models
from categories.views import CategoryApiViewSet

router_categories = DefaultRouter()
router_categories.register(prefix='categories', basename='categories', viewset=CategoryApiViewSet)