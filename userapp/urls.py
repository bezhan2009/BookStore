from django.urls import path
from .views import UserProfileView, UserProfileDetails

urlpatterns = [
    path('sign-up/', UserProfileView.as_view(), name='sign-up'),
    path('details/', UserProfileDetails.as_view(), name='user-details'),
]
