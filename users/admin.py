# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Local Models
from users.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
  pass