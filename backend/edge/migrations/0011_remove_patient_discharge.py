# Generated by Django 5.0.6 on 2024-06-14 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edge', '0010_room_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='discharge',
        ),
    ]
