from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from users.permissions import EmployeePermissions

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [EmployeePermissions]