# Generated by Django 5.2.2 on 2025-06-12 03:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_remove_cliente_direccion_remove_cliente_usuario_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
