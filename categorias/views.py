from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Categoria
from .serializers import CategoriaSerializer

from rest_framework.permissions import IsAuthenticated

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

