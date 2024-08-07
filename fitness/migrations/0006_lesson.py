# Generated by Django 5.0.6 on 2024-07-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fitness", "0005_image_delete_service"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lesson",
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
                ("name", models.TextField()),
                ("body", models.TextField()),
                ("slug", models.SlugField()),
            ],
        ),
    ]
