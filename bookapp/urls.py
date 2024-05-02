from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookView.as_view(), name='book-view'),
    path('book-details/', views.BookDetailView.as_view(), name='book-detail-view'),
]
