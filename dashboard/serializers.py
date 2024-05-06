from rest_framework import serializers
from .models import Product , Category, Sale


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'brand', 'price', 'discount_price',  'category',  'sold',  'quantity_value', 'quantity_type')

