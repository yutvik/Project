# Generated by Django 4.2.1 on 2023-07-19 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_buyer', '0008_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='pro_id',
        ),
    ]
