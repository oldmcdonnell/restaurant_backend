# Generated by Django 5.0.6 on 2024-05-23 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TNP_app', '0003_order_food_item_customerreview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food_type',
            new_name='category',
        ),
    ]