from django.shortcuts import render

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['name', 'price', 'stock']
    ordering_fields = ['price', 'name']
    ordering = ['name']

# Create your views here.
