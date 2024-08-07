# Generated by Django 5.0.6 on 2024-07-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fitness", "0006_lesson"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(max_length=75)),
                ("body", models.TextField()),
                ("slug", models.SlugField()),
            ],
        ),
    ]
