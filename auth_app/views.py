from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from auth_app.serializers import CompanyCreateSerializer


# Create your views here.
class CompanyCreateView(CreateAPIView):
    serializer_class = CompanyCreateSerializer
