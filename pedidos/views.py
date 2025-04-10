from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.permissions import IsAuthenticated

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):  # ¡Ahora está dentro de la clase!
        pedido = serializer.save()
        producto = pedido.producto
        producto.stock -= pedido.cantidad
        producto.save()

    def perform_destroy(self, instance):
        producto = instance.producto
        producto.stock += instance.cantidad
        producto.save()
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Pedido eliminado"}, status=status.HTTP_200_OK)