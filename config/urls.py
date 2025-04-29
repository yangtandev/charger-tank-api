from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/charger-tank/', include('charger_tank.urls')),
    path('api/v1/clientsetting/', include('clientsetting.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
