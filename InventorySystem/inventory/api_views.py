from rest_framework import generics
from .models import InventoryItem, SubItem
from .serializers import InventoryItemSerializer, SubItemSerializer

class InventoryItemListCreate(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class SubItemListCreate(generics.ListCreateAPIView):
    queryset = SubItem.objects.all()
    serializer_class = SubItemSerializer