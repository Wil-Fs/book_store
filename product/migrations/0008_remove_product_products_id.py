# Generated by Django 5.0.6 on 2024-06-01 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0007_alter_product_price"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="products_id",
        ),
    ]
