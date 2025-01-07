
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'stock_quantity', 'image_url', 'created_date']
        read_only_fields = ['created_date']