# Generated by Django 5.0.6 on 2024-07-03 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TNP_app', '0007_alter_customerreview_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='food_item',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='orders', through='TNP_app.OrderItem', to='TNP_app.food'),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='TNP_app.order'),
        ),
    ]
