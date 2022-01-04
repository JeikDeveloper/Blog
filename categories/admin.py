# Django
from django.contrib import admin

# Local Models
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['title', 'published']