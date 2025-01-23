from . import views
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='index'),  # Página principal
    path('admin/', admin.site.urls),      # Panel de administración
    path('', include('core.urls')),  # Ruta para la app core (anteriormente cognify)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
