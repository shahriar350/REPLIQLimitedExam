from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class CompanyDevice(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_company_devices")
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_employees")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="get_employee")
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.user.name


class EmployeeDevices(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_company_devices_infos")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_employee_devices")
    device = models.OneToOneField(CompanyDevice, on_delete=models.CASCADE, related_name="get_employees",
                                  primary_key=True)
    checked_out = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True)


class EmployeeDeviceLog(models.Model):
    log = models.CharField(max_length=255)
    employee_device = models.ForeignKey(EmployeeDevices, on_delete=models.CASCADE, related_name="get_employee_device_logs")
    date_created = models.DateTimeField(auto_now_add=True)
