from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'brand', 'price', 'discount_price',  'category', 'sub_category', 'sold',  'quantity_value', 'quantity_type')
      