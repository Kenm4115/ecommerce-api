
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters


# Create a filter class for the Product model
class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category', label='Category')
    min_price = filters.NumberFilter(field_name='price', label='Min Price')
    max_price = filters.NumberFilter(field_name='price', label='Max Price')
    in_stock = filters.BooleanFilter(
        field_name='stock_quantity', label='In Stock', method='filter_in_stock')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'in_stock']

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock_quantity__gt=0) # Filter products with stock quantity greater than 0
        return queryset

# Product viewset
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend, SearchFilter] # Enable both filtering and search functionality
    filterset_class = ProductFilter # Use our custom ProductFilter
    search_fields = ['name', 'category'] # Allow search by product name and category
    
