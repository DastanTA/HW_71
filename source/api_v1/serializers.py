from django.contrib.auth import get_user_model
from rest_framework import serializers
from ebay.models import Product, Order, OrderProduct, Basket


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'remainder', 'price']
        read_only_fields = ['id']


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['id', 'product', 'order', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    order_product = OrderProductSerializer(many=True, read_only=True)
   
    class Meta:
        model = Order
        fields = ['id', 'order_product', 'user', 'created_at']
        read_only_fields = ['id', 'created_at']


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ['id', 'product', 'quantity']
