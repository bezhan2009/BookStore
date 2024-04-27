from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserProfileSerializer
import logging


logger = logging.getLogger('django')


class UserProfileView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
            'address': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'phone_number': openapi.Schema(type=openapi.TYPE_INTEGER),
        }
    ))
    def post(self, request):
        """
                Создает нового пользователя.

                Свойства для создания нового пользователя:
                - username: Имя пользователя
                - password: Пароль
                - address: Address пользователя
                - email: Email пользователя
                - phone_number: Телефонный номер пользователя
                """
        data = {
            'username': request.data['username'],
            'password': request.data['password'],
            'address': request.data['address'],
            'email': request.data['email'],
            'phone_number': request.data['phone_number'],
        }
        serializer = UserProfileSerializer(data=data)

        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            refresh = RefreshToken.for_user(user)
            logger.info(f"New user created with ID {user.id}.")

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
