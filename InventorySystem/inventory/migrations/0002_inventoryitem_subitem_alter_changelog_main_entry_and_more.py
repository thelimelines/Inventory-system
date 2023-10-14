# Generated by Django 4.2.6 on 2023-10-14 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('parent_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subitems', to='inventory.inventoryitem')),
            ],
        ),
        migrations.AlterField(
            model_name='changelog',
            name='main_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventoryitem'),
        ),
        migrations.DeleteModel(
            name='MainEntry',
        ),
    ]
