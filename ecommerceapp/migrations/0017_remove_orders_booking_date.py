# Generated by Django 4.2.5 on 2023-09-27 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0016_alter_orders_booking_date"),
    ]

    operations = [
        migrations.RemoveField(model_name="orders", name="booking_date",),
    ]
