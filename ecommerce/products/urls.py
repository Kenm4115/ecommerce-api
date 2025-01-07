
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet) # Register the Product ViewSet with the router

urlpatterns = [
    path('', include(router.urls)),
    path('products/', views.get_all_products, name='get_all_products'),
]

urlpatterns += [
    path('products/create/', views.create_product, name='create_product'),
]
