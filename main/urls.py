"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog.views import pagina_apicultura, pagina_alimentos, pagina_informatica, pagina_inicial


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_inicial, name='pagina_inicial'),
    path('pagina_apicultura/', pagina_apicultura, name='pagina_apicultura'),
    path('pagina_alimentos/', pagina_alimentos, name='pagina_alimentos'),
    path('pagina_informatica/', pagina_informatica, name='pagina_informatica'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
