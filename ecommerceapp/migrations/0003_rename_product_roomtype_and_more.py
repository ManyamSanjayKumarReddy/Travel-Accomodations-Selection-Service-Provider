# Generated by Django 4.2.5 on 2023-09-23 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0002_product"),
    ]

    operations = [
        migrations.RenameModel(old_name="Product", new_name="RoomType",),
        migrations.RenameField(
            model_name="roomtype", old_name="product_name", new_name="room_name",
        ),
    ]
