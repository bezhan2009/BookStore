from django.urls import path
from orderapp import views


urlpatterns = [
    path('', views.OrderView, name='Order-View'),
    path('detail/', views.OrderDetail, name='Order-Detail'),
]
