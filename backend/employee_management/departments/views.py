from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentSerializer
from companies.permissions import IsAdminOrManager

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrManager]

    def perform_create(self, serializer):
        # Automatically set the creator
        serializer.save(created_by=self.request.user)