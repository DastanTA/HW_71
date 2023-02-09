from django.contrib import admin
from django.urls import path, include


api_urls = [
    path('v1/', include('api_v1.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ebay.urls')),
    path('api/', include(api_urls)),
    path('accounts/', include('accounts.urls')),
]
