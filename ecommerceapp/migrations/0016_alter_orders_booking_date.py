# Generated by Django 4.2.5 on 2023-09-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0015_alter_orders_booking_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="booking_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]