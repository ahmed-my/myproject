# Generated by Django 5.0.6 on 2024-07-20 20:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fitness", "0010_home"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="banner",
        ),
    ]
