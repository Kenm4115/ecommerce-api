
from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDeleteView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-detail'),
]
