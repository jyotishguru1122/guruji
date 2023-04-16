# Generated by Django 4.2 on 2023-04-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("image", models.ImageField(upload_to="images/")),
                ("heading", models.CharField(max_length=200)),
                ("description", models.TextField(max_length=255)),
                ("long_description", models.TextField(max_length=8000)),
            ],
        ),
    ]
