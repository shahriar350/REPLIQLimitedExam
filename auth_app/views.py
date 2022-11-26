from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from auth_app.serializers import CompanyCreateSerializer, LoginViewSerializer


# Create your views here.
class CompanyCreateView(CreateAPIView):
    serializer_class = CompanyCreateSerializer


class LoginView(CreateAPIView):
    serializer_class = LoginViewSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data.get('phone_number'),
                            password=serializer.validated_data.get('password'))
        if user:
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            return Response(status=200, data={
                "key": token.key,
                "user": user.name
            })
