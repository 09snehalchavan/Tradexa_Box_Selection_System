from django.urls import path
from .views import (
    BoxListAPIView,
    RecommendBoxAPIView,
    OrderListAPIView,
)

urlpatterns = [
    path('boxes/', BoxListAPIView.as_view(), name='box-list'),
    path('recommend-box/', RecommendBoxAPIView.as_view(), name='recommend-box'),
    path('orders/', OrderListAPIView.as_view(), name='order-list'),
]