from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import mixins

from api_v1.serializers import ProductSerializer, OrderSerializer
from ebay.models import Product, Order


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderRetrieveCreateViewSet(ViewSet):
    
    def retrieve(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=kwargs.get('pk'))
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
