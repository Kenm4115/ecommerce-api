
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet) # Register the Product ViewSet with the router

urlpatterns = [
    path('', include(router.urls)),
]
