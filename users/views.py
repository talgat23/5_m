import random

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from users.models import UserConfirmation
from users.serializers import UserRegisterSerializer, UserConfirmationSerializer, UserLoginSerializer


# @api_view(['POST'])
# def register_api_view(request):
#     serializer = UserRegisterSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = User.objects.create_user(**serializer.validated_data, is_active=False)
#     confirm = UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
#     return Response({'status': 'User registered', 'code': confirm.code, 'data': serializer.data},
#                     status=HTTP_201_CREATED)


class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data, is_active=False)
        confirm = UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
        return Response({'status': 'User registered', 'code': confirm.code, 'data': serializer.data},
                        status=HTTP_201_CREATED)


# @api_view(['POST'])
# def confirm_api_view(request):
#     serializer = UserConfirmationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     code = serializer.validated_data.get('code')
#     confirm = get_object_or_404(UserConfirmation, code=code)
#     user = confirm.user
#     user.is_active = True
#     user.save()
#     confirm.delete()
#     return Response({'status': 'User activated'}, status=status.HTTP_200_OK)


class ConfirmAPIView(APIView):
    serializer_class = UserConfirmationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')
        confirm = get_object_or_404(UserConfirmation, code=code)
        user = confirm.user
        user.is_active = True
        user.save()
        confirm.delete()
        return Response({'status': 'User activated'}, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def login_api_view(request):
#     serializer = UserLoginSerializer(data=request.data)
#     serializer.is_valid()
#     user = authenticate(**serializer.validated_data)
#     login(request, user)
#
#     if user:
#         token, created = Token.objects.get_or_create(user=user)
#         user.save()
#         return Response({'token': token.key})
#     return Response({'error': 'Invalid credentials'}, status=400)

class LoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = authenticate(**serializer.validated_data)
        login(request, user)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            user.save()
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)
