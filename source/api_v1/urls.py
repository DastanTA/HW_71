from django.urls import path, include
from rest_framework import routers
from api_v1 import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderRetrieveCreateViewSet, basename='order')

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]