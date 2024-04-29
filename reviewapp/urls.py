from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewView.as_view(), name='review-view'),
    path('details/', views.ReviewDetail.as_view(), name='review-detail'),
]
