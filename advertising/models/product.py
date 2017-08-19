from django.db import models


class Product(models.Model):
    prd_key = models.IntegerField(
        verbose_name="Product Key",
        help_text="Id of the product, unique identifier of the product at its origin.")
    prd_name = models.CharField(
        verbose_name="Name",
        max_length=30)
    prd_description = models.CharField(
        verbose_name="Description",
        max_length=255)
