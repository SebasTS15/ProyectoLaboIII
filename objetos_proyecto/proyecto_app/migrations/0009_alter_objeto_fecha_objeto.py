# Generated by Django 5.0.4 on 2024-06-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0008_remove_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objeto',
            name='fecha_objeto',
            field=models.DateField(auto_now_add=True),
        ),
    ]
