# Generated by Django 5.0.4 on 2024-05-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0003_objeto_lugar_perdiad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='sexo',
            field=models.CharField(blank=True, default=' ', max_length=1, null=True),
        ),
    ]
