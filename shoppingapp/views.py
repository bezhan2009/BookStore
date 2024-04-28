from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.tokens import get_user
from .models import ShoppingCart
from .serializers import ShoppingCartSerializer
import logging


logger = logging.getLogger('shoppingapp.views')


class ShoppingCartView(APIView):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
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
        return Response(status=status.HTTP_204_NO_CONTENT)
