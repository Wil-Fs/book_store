from django.db import models


from .category import Category


class Product(models.Model):
    products_id = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)