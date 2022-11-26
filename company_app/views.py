from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response

from company_app.middlewares import IsCompany
from company_app.models import EmployeeDeviceLog, EmployeeDevices
from company_app.serializers import CompanyCreateEmpSerializer, CompanyDeviceSerializer, EmployeeDevicesSerializer, \
    EmployeeReturnDeviceSerializer
from rest_framework.authentication import TokenAuthentication

class CompanyCreateUserView(CreateAPIView):
    serializer_class = CompanyCreateEmpSerializer
    permission_classes = [IsCompany]


class CompanyDeviceCreateView(CreateAPIView):
    serializer_class = CompanyDeviceSerializer
    permission_classes = [IsCompany]
    authentication_classes = [TokenAuthentication]

class ProvideDeviceToEmployee(CreateAPIView):
    serializer_class = EmployeeDevicesSerializer
    permission_classes = [IsCompany]
    authentication_classes = [TokenAuthentication]


class ProvideDeviceUpdateToEmployee(CreateAPIView):
    serializer_class = EmployeeReturnDeviceSerializer
    permission_classes = [IsCompany]
    authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        try:
            emp = EmployeeDevices.objects.get(device=self.kwargs.get('pk'))
            if emp.returned:
                return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY, data="Product returned")
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            emp.returned = serializer.validated_data.get('returned')
            emp.save()
            EmployeeDeviceLog.objects.create(employee_device=emp, log=serializer.validated_data.get('log'))
            return Response(status=200, data=serializer.validated_data)
        except EmployeeDevices.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


