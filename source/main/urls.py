from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


api_urls = [
    path('v1/', include('api_v1.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ebay.urls')),
    path('api/', include(api_urls)),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
