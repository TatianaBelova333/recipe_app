# Generated by Django 4.2.4 on 2023-08-31 15:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredientamount",
            name="amount",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=1,
                        message="Количество должно быть целым числом больше 0.",
                    ),
                    django.core.validators.MaxValueValidator(
                        limit_value=2000, message="Количество должно не более 2000."
                    ),
                ],
                verbose_name="Количество",
            ),
        ),
        migrations.AddConstraint(
            model_name="recipeingredientamount",
            constraint=models.UniqueConstraint(
                fields=("recipe", "ingredient_unit"),
                name="unique_recipe_ingredient_unit",
            ),
        ),
    ]
