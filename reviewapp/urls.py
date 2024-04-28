from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewView, name='review-view'),
    path('detail/', views.ReviewDetail, name='review-detail'),
]
