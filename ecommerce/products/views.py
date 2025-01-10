
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer
from django.db.models import Q
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['name', 'category']  # Searchable fields

    def get_queryset(self):
        queryset = super().get_queryset()
        # Optionally, filter by stock availability (if implemented later)
        stock_available = self.request.query_params.get('in_stock', None)
        if stock_available:
            queryset = queryset.filter(stock_quantity__gt=0)  # Stock > 0
        return queryset

    def get_queryset(self):
        queryset = super().get_queryset()

        # Optional filters
        category_filter = self.request.query_params.get('category', None)
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        stock_available = self.request.query_params.get('in_stock', None)

        if category_filter:
            queryset = queryset.filter(category__icontains=category_filter)

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if stock_available:
            queryset = queryset.filter(
                stock_quantity__gt=0)  # Only in-stock items

        return queryset


class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
