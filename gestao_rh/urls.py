from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('funcionario/', include('apps.funcionario.urls')),
    path('admin/', admin.site.urls),
]
