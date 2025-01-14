# Generated by Django 5.0.6 on 2024-06-18 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edge', '0019_alter_doctor_age_alter_doctor_bank_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='bank',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='biography',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='date_of_appointment',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor_first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor_last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='roomnumber',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
