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


# class OrderSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     order_product = OrderProductSerializer(many=True)
   
#     class Meta:
#         model = Order
#         fields = ['id', 'order_product', 'user', 'created_at']
#         read_only_fields = ['id', 'created_at']

#     def create(self, validated_data):
#         order_products_data = validated_data.pop('order_products')
#         order = Order.objects.create(**validated_data)
#         for order_product_data in order_products_data:
#             OrderProduct.objects.create(order=order, **order_product_data)
#         return order


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ['id', 'product', 'quantity']
