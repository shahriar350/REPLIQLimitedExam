from . import views
from django.urls import path

urlpatterns = [
    path('create/company/', views.CompanyCreateView.as_view()),

]
