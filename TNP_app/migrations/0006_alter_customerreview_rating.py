# Generated by Django 5.0.6 on 2024-07-03 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TNP_app', '0005_rename_name_food_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerreview',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
