# Generated by Django 5.1.4 on 2024-12-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='hecho',
            field=models.BooleanField(default=False),
        ),
    ]
