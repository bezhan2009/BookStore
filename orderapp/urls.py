from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrderView.as_view(), name='order-view'),
    path('details/', views.OrderDetail.as_view(), name='Order-Detail'),
]
