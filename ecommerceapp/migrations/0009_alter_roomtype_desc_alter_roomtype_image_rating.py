# Generated by Django 4.2.5 on 2023-09-25 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ecommerceapp", "0008_roomtype_image6"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomtype", name="desc", field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="roomtype",
            name="image",
            field=models.ImageField(default="", upload_to="images/images"),
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.IntegerField(default=0)),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ecommerceapp.roomtype",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]