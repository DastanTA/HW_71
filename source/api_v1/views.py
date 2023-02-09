from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response

from api_v1.serializers import ProductSerializer, OrderSerializer
from ebay.models import Product, Order


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(ViewSet):
    def retrieve(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=kwargs.get("pk"))
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def create(self, request):
        serilizer = OrderSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors, status=400)
