from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Review
from .serializers import ReviewSerializer
from utils.tokens import get_user_id_from_token
from userapp.models import UserProfile
import logging

logger = logging.getLogger('reviewapp.views')


def get_user(request):
    user_id = get_user_id_from_token(request)
    user = UserProfile.objects.get(id=user_id)
    return user


class ReviewView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = get_user(request)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    def put(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        user = get_user(request)
        review = get_object_or_404(Review, pk=review_id, user=user)
        review.delete()
        return Response({"message": "Review has been successfully removed."}, status=status.HTTP_200_OK)
