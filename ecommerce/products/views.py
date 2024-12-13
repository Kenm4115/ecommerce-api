from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_products(request):
    products = Product.objects.all().values(
        "id", "name", "category", "description", "price", "stock")
    return JsonResponse(list(products), safe=False)


# Create your views here.
