# Generated by Django 5.0.3 on 2024-03-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Category", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
