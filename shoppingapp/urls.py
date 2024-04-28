from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingCartView, name='shopping-cart-view'),
    path('detail/', views.ShoppingCartDetailView.as_view(), name='shopping-cart-detail'),
]
