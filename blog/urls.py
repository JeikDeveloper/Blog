# Django
from django.contrib import admin
from django.urls import path, include

# OpenAPI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Local Models
from categories.urls import router_categories
from posts.urls import router_posts
from comments.urls import router_comments

schema_view = get_schema_view(
 openapi.Info(
  title="Blog API",
  default_version='v1',
  description="Documentacion de la API",
  terms_of_service="",
  contact=openapi.Contact(email="contact@snippets.local"),
  license=openapi.License(name="BSD License"),
 ),
 public=True,
 #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  path('api/', include('users.urls')),
  path('api/', include(router_categories.urls)),
  path('api/', include(router_posts.urls)),
  path('api/', include(router_comments.urls)),
]
