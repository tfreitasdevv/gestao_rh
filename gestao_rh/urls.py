from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionario/', include('apps.funcionario.urls')),
    path('departamento/', include('apps.departamento.urls')),
    path('documento/', include('apps.documento.urls')),
    path('empresa/', include('apps.empresa.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
