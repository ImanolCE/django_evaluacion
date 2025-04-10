# pedidos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)  # Endpoint: /api/pedidos/

urlpatterns = [
    path('', include(router.urls)),  # este incluye las rutas generadas
]
