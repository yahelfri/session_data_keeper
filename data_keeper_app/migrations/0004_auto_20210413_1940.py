# Generated by Django 3.1.7 on 2021-04-13 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_keeper_app', '0003_user_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_details',
            new_name='UserDetails',
        ),
    ]