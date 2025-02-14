from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet

# Crea el enrutador para las categorías
router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

# Define las rutas
urlpatterns = [
    path('', include(router.urls)),
]

