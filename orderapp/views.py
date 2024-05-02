from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order  # Импорт модели внутри функции представления
from .serializers import OrderSerializer
from utils.tokens import get_user_id_from_token
from userapp.models import UserProfile
import logging

logger = logging.getLogger('orderapp.views')


def get_user(request):
    user_id = get_user_id_from_token(request)
    user = UserProfile.objects.get(id=user_id)
    return user


class OrderView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = get_user(request)
        orders = Order.objects.filter(user_id=user.id)
        serializer = OrderSerializer(orders, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK)

    def post(self, request):
        user = get_user(request)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED)
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    def delete(self, request, order_pk):
        user = get_user(request)
        order = get_object_or_404(Order, pk=order_pk)
        order.delete()
        return Response(
                data={'message': f'Order with id {order_pk} has been removed successfully'},
                status=status.HTTP_200_OK)