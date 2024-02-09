# Generated by Django 5.0.1 on 2024-01-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shoping", "0003_alter_category_description_alter_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reviews",
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
                ("title", models.CharField(max_length=100, verbose_name="заголовок")),
                ("slug", models.CharField(max_length=200, verbose_name="slug")),
                (
                    "content",
                    models.TextField(max_length=1000, verbose_name="содержание"),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="preview/",
                        verbose_name="превью",
                    ),
                ),
                ("date_of_creation", models.DateTimeField(auto_now_add=True)),
                ("publication_sign", models.BooleanField(default=False)),
                ("number_of_views", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name": "отзыв",
                "verbose_name_plural": "отзывы",
            },
        ),
    ]