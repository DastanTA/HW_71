from django.urls import path, include
from rest_framework import routers
from api_v1 import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]