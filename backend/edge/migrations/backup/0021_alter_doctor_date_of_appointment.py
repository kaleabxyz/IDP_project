# Generated by Django 5.0.6 on 2024-06-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edge', '0020_alter_doctor_age_alter_doctor_bank_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='date_of_appointment',
            field=models.DateField(default='2024-06-14', null=True),
        ),
    ]