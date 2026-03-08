from django.contrib import admin
from django.urls import path, include # <-- Vérifie bien que "include" est ici
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # <-- C'est cette ligne qui redirige l'accueil
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)