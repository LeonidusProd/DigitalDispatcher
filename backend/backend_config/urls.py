from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from backend_config import settings
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    # path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include('api_v1.urls'), name='api_v1'),
    path('admin/', admin.site.urls, name='admin'),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
