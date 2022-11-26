from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from auth_app.models import User
from company_app.models import Employee, CompanyDevice, EmployeeDevices, EmployeeDeviceLog


class CompanyCreateEmpSerializer(serializers.Serializer):
    company = serializers.HiddenField(default=serializers.CurrentUserDefault())
    phone_number = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    role_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        user = User.objects.create_company_staff(
            name=validated_data.get('name'), phone_number=validated_data.get('phone_number'),
            password=validated_data.get('password')
        )
        Employee.objects.create(company=validated_data.get('company'), user=user, role=validated_data.get('role_name'))
        return validated_data


class CompanyDeviceSerializer(serializers.ModelSerializer):
    company = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CompanyDevice
        fields = "__all__"


class EmployeeDevicesSerializer(serializers.ModelSerializer):
    company = serializers.HiddenField(default=serializers.CurrentUserDefault())
    log = serializers.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        user = kwargs['context']['request'].user
        super(EmployeeDevicesSerializer, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = User.objects.filter(
            id__in=user.get_employees.all().values_list('id', flat=True)).all()
        self.fields['device'].queryset = user.get_company_devices.all()

    class Meta:
        model = EmployeeDevices
        fields = "__all__"

    def validate(self, data):
        if not data['company'].get_employees.filter(id=data['employee'].id).exists():
            raise ValidationError({'employee': 'Invalid employee or wrong employee'})
        if not data['company'].get_company_devices.filter(id=data['device'].id).exists():
            raise ValidationError({'device': 'Invalid device or wrong device'})
        return data

    def create(self, validated_data):
        emp = EmployeeDevices.objects.create(company=validated_data.get('company'), device=validated_data.get('device'),
                                             employee=validated_data.get('employee'))
        EmployeeDeviceLog.objects.create(employee_device=emp, log=validated_data.get('log'))
        return validated_data


class EmployeeReturnDeviceSerializer(serializers.Serializer):
    returned = serializers.DateTimeField()
    log = serializers.CharField(max_length=255)

