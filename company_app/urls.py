from . import views
from django.urls import path

urlpatterns = [
    path('create/staff/', views.CompanyCreateUserView.as_view()),
    path('create/device/', views.CompanyDeviceCreateView.as_view()),
    path('provide/device/emplyee/',views.ProvideDeviceToEmployee.as_view()),
    path('provide/device/emplyee/<int:pk>/',views.ProvideDeviceUpdateToEmployee.as_view()),
]
