from django.urls import path, include


app_name = 'api_v1'

product_urls = [

]

urlpatterns = [
    path('product/', include(product_urls)),
]