from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingCartView.as_view(), name='shopping-cart-view'),
    path('details/', views.ShoppingCartDetailView.as_view(), name='shopping-cart-detail'),
]
