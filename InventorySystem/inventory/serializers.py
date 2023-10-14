from rest_framework import serializers
from .models import InventoryItem, SubItem

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class SubItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubItem
        fields = '__all__'