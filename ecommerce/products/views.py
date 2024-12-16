
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



def get_all_products(request):
    products = Product.objects.all().values(
        "id", "name", "category", "description", "price", "stock")
    return JsonResponse(list(products), safe=False)

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            name = data['name'],
            category = data['category'],
            description = data['description'],
            price = data['price'],
            stock = data['stock']
        )
        return JsonResponse({"id": product.id, "message": "Product created successfully!"}, status=201)

# Create your views here.
