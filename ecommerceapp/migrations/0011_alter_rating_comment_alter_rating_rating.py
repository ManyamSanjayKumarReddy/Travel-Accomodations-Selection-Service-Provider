# Generated by Django 4.2.5 on 2023-09-26 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0010_rating_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating", name="comment", field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name="rating", name="rating", field=models.IntegerField(),
        ),
    ]
