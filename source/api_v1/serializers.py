from rest_framework import serializers
from ebay.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'remainder', 'price']
        read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'user', 'created_at']
        read_only_fields = ['id', 'created_at']