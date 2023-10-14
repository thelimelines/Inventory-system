from django.contrib import admin
from .models import InventoryItem, ChangeLog

admin.site.register(InventoryItem)
admin.site.register(ChangeLog)