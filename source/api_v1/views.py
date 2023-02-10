from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from api_v1.serializers import ProductSerializer, OrderSerializer, BasketSerializer
from ebay.models import Product, Order, Basket, OrderProduct


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return super().get_permissions()


# class OrderRetrieveCreateViewSet(ViewSet):
#     permission_classes = [IsAdminUser]

#     def create(self, request, *args, **kwargs):
#         basket = Basket.objects.all()
#         user = get_user_model().objects().get(pk=request.body.get('user'))
#         order = Order.objects.create(user=user)

#         for item in basket:
#             OrderProduct.objects.create(product=item.product, quantity=item.quantity, order=order)
#             item.product.remainder -= item.quantity
#             item.product.save()
#             item.delete()

#         serializer = OrderSerializer(order)
#         return Response(serializer.data)

#     def retrieve(self, request, *args, **kwargs):
#         order = get_object_or_404(Order, pk=kwargs.get("pk"))
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)



class OrderRetrieveCreateViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAdminUser]

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return []
    #     return super().get_permissions()


class BasketListAddDeleteViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
