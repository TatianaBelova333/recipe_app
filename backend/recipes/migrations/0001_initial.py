# Generated by Django 4.2.4 on 2023-08-30 22:58

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredient",
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
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=200,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ингредиент",
                "verbose_name_plural": "Ингредиенты",
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="IngredientUnit",
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
            ],
            options={
                "verbose_name": "Ингредиент с единицой измерения",
                "verbose_name_plural": "Ингредиенты с единицами измерения",
                "ordering": ("ingredient", "measurement_unit"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MeasurementUnit",
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
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=200,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
            ],
            options={
                "verbose_name": "Единица измерения",
                "verbose_name_plural": "Единицы измерения",
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Recipe",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=200, verbose_name="Название"
                    ),
                ),
                ("text", models.TextField(verbose_name="Описание рецепта")),
                (
                    "cooking_time",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=1,
                                message="Время приготовления должно быть больше 0.",
                            ),
                            django.core.validators.MaxValueValidator(
                                limit_value=360,
                                message="Время приготовления должно быть не более 360 мин.",
                            ),
                        ],
                        verbose_name="Время приготовления (мин.)",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="recipes/images/", verbose_name="Избражение рецепта"
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Дата публикации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
                "ordering": ("-pub_date", "name"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=200,
                        unique=True,
                        verbose_name="Название",
                    ),
                ),
                (
                    "color",
                    colorfield.fields.ColorField(
                        default="#FF0000",
                        image_field=None,
                        max_length=18,
                        samples=None,
                        unique=True,
                        verbose_name="Цвет тега",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=200, unique=True, verbose_name="slug"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
                "ordering": ("name",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RecipeIngredientAmount",
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
                    "amount",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=1,
                                message="Количество должно быть больше 0.",
                            )
                        ],
                        verbose_name="Количество",
                    ),
                ),
                (
                    "ingredient_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="recipes.ingredientunit",
                        verbose_name="Ингредиент с ед.изм.",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes.recipe",
                        verbose_name="Рецепт",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ингредиент, ед. измер., кол-во",
                "verbose_name_plural": "Ингредиенты, ед. измер., кол-во",
            },
        ),
    ]
