# Generated by Django 5.0.6 on 2024-06-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='furst_name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='biography',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='guardian',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.CharField(max_length=5),
        ),
    ]
