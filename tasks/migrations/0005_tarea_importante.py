# Generated by Django 5.1.4 on 2024-12-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_tarea_fecha_limite'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='importante',
            field=models.BooleanField(default=False),
        ),
    ]