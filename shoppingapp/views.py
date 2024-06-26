from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer
from utils.tokens import get_user_id_from_token
from userapp.models import UserProfile
import logging

logger = logging.getLogger('shoppingapp.views')


def get_user(request):
    user_id = get_user_id_from_token(request)
    user = UserProfile.objects.get(id=user_id)
    return user


class ShoppingCartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = get_user(request)
        cart_items = ShoppingCart.objects.filter(user_id=user.id)
        serializer = ShoppingCartSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = get_user(request)
        serializer = ShoppingCartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShoppingCartDetailView(APIView):
    def delete(self, request, item_id):
        item = get_object_or_404(ShoppingCart, pk=item_id)
        item.delete()
        return Response({"message": "ShopppingCart has been successfully removed."},status=status.HTTP_200_OK)
