# Generated by Django 4.2.5 on 2023-09-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0006_rename_product_roomtype_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="roomtype",
            name="image1",
            field=models.ImageField(default="", upload_to="images/additional-images"),
        ),
        migrations.AddField(
            model_name="roomtype",
            name="image2",
            field=models.ImageField(default="", upload_to="images/additional-images"),
        ),
        migrations.AddField(
            model_name="roomtype",
            name="image3",
            field=models.ImageField(default="", upload_to="images/additional-images"),
        ),
        migrations.AddField(
            model_name="roomtype",
            name="image4",
            field=models.ImageField(default="", upload_to="images/additional-images"),
        ),
        migrations.AddField(
            model_name="roomtype",
            name="image5",
            field=models.ImageField(default="", upload_to="images/additional-images"),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="image",
            field=models.ImageField(default="", upload_to="images/additional-images"),
        ),
    ]
