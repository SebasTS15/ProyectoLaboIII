# Generated by Django 5.0.4 on 2024-06-03 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0007_user_delete_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
