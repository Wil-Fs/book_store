# Generated by Django 5.0.6 on 2024-06-04 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0009_product_products_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="products_id",
        ),
    ]
