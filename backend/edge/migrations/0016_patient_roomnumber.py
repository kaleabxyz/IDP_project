# Generated by Django 5.0.6 on 2024-06-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edge', '0015_patient_doctor_first_name_patient_doctor_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='roomnumber',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
