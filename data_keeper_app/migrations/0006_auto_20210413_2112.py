# Generated by Django 3.1.7 on 2021-04-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_keeper_app', '0005_auto_20210413_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
