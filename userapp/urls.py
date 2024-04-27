from django.urls import path

from .views import UserProfileView

urlpatterns = [
    path('sign-up/', UserProfileView.as_view(), name='sign_up'),
]
