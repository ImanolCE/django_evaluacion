"""
URL configuration for django_evaluacion project.

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
from django.urls import path, include

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    # path('api/auth/', include('django.contrib.auth.urls')),
    path('api/auth/', include('authentication.urls')),
    path('api/', include('productos.urls')),
    path('api/', include('categorias.urls')),

    path('api/', include('clientes.urls')),  # Ruta para clientes
    path('api/', include('pedidos.urls')),   # Ruta para pedidos

    # token de acceso para cuando un usuario inicia sesion
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 

    # este genera un nuevo token, cuando el anterior expria, para que no se vulelva a inicar sesion
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]
