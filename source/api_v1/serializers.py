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
        fields = ['id', 'product', 'quantity']
        read_only_fields = ['id']


class OrderCreateSerializer(serializers.ModelSerializer):
    order_products = serializers.ListField(write_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'order_products']

    def create(self, validated_data):
        order_products_data = validated_data.pop('order_products')
        order = Order.objects.create(**validated_data)
        for order_product in order_products_data:
            OrderProduct.objects.create(order=order, product_id=order_product['product'], quantity=order_product['quantity'])
        return order


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # order_product = OrderProductSerializer(many=True, read_only=True)
   
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['products'] = ProductSerializer(instance.products.all(), many=True).data
        return data

    class Meta:
        model = Order
        fields = ['id', 'products', 'user', 'created_at']
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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = ProductSerializer(instance.products.all(), many=True).data
        return data

    class Meta:
        model = Basket
        fields = ['id', 'product', 'quantity']
