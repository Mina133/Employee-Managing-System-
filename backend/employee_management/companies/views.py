from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Company
from .serializers import CompanySerializer
from .permissions import IsAdminOrManager

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminOrManager]  # Use custom permission

    def perform_create(self, serializer):
        # Automatically set the creator as the current user
        serializer.save(created_by=self.request.user)