# Generated by Django 5.0.6 on 2024-06-18 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edge', '0022_alter_doctor_date_of_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='date_of_appointment',
            field=models.DateField(default='2024-06-04'),
        ),
    ]
