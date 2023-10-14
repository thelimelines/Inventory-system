from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    notes = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class SubItem(models.Model):
    parent_item = models.ForeignKey(InventoryItem, related_name='subitems', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class ChangeLog(models.Model):
    username = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    changed_fields = models.JSONField()
    main_entry = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)

@receiver(post_save, sender=InventoryItem)
@receiver(post_save, sender=SubItem)
def create_change_log_on_save(sender, instance, **kwargs):
    # Logic to create ChangeLog instance
    ChangeLog.objects.create(
        username="username_here",  # Replace with actual username
        changed_fields="fields_here",  # Replace with actual changed fields
        main_entry=instance if isinstance(instance, InventoryItem) else instance.parent_item
    )

@receiver(post_delete, sender=InventoryItem)
@receiver(post_delete, sender=SubItem)
def create_change_log_on_delete(sender, instance, **kwargs):
    # Logic to create ChangeLog instance
    ChangeLog.objects.create(
        username="username_here",  # Replace with actual username
        changed_fields="fields_here",  # Replace with actual changed fields
        main_entry=instance if isinstance(instance, InventoryItem) else instance.parent_item
    )