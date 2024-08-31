from rest_framework import serializers
from .models import ClothingItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingItem
        fields = ['name', 'description', 'price', 'image']
