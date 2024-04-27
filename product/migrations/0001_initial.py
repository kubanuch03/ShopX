# Generated by Django 5.0.3 on 2024-04-20 06:33

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Category", "0001_initial"),
        ("app_userseller", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RecallImages",
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
                (
                    "images",
                    models.ImageField(
                        blank=True, null=True, upload_to="recall_image/%Y/%m/%d/"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Size",
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
                ("title", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("discount", models.PositiveIntegerField(blank=True, null=True)),
                ("slug", models.SlugField(max_length=200)),
                (
                    "image1",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%Y/%m/%d"
                    ),
                ),
                (
                    "image2",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%Y/%m/%d"
                    ),
                ),
                (
                    "image3",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%Y/%m/%d"
                    ),
                ),
                (
                    "image4",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%Y/%m/%d"
                    ),
                ),
                ("available", models.BooleanField(default=True)),
                ("location", models.CharField(blank=True, max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="Category.category",
                    ),
                ),
                (
                    "podcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pod_products",
                        to="Category.podcategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        limit_choices_to={"is_seller": True},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="app_userseller.sellerprofile",
                    ),
                ),
                ("size", models.ManyToManyField(to="product.size")),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Like",
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Лайк",
                "verbose_name_plural": "Лайки",
            },
        ),
        migrations.CreateModel(
            name="Recall",
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
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                ("text", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("recall_images", models.ManyToManyField(to="product.recallimages")),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
            },
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["id", "slug"], name="product_pro_id_b9e5a0_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["name"], name="product_pro_name_b60cd1_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["price"], name="product_pro_price_3acd1d_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(
                fields=["-created"], name="product_pro_created_942044_idx"
            ),
        ),
    ]
