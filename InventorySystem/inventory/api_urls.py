from django.urls import path
from . import api_views

urlpatterns = [
    path('inventory/', api_views.InventoryItemListCreate.as_view(), name='inventory-list-create'),
    path('subitem/', api_views.SubItemListCreate.as_view(), name='subitem-list-create'),
]