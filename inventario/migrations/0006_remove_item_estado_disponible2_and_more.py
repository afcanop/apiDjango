# Generated by Django 4.1.2 on 2022-10-27 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_item_estado_disponible3_item_estado_disponible4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='estado_disponible2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='estado_disponible3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='estado_disponible4',
        ),
    ]
