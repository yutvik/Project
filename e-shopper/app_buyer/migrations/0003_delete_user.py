# Generated by Django 4.2.1 on 2023-07-05 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_buyer', '0002_user_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
