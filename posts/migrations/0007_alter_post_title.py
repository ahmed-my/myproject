# Generated by Django 5.0.6 on 2024-07-21 01:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0006_alter_post_slug_alter_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=75),
        ),
    ]