from django.contrib import admin
from .models import ClothingItem  # Ensure this matches the model name


@admin.register(ClothingItem)
class ClothingItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
