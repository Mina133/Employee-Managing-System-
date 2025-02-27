from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    num_departments = serializers.ReadOnlyField()
    num_employees = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'num_departments', 'num_employees']