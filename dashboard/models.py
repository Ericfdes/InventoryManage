from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    absolute_url = models.URLField()
    sold = models.IntegerField()
    temperature = models.CharField(max_length=10)
    quantity_value = models.FloatField(null=True)
    quantity_type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.product_name
    