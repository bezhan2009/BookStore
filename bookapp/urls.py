from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView, name='Book-View'),
    path('detail/', views.BookDetailView, name='Book-Detail-View'),
]
