from rest_framework import serializers
from .models import Department
from companies.models import Company

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'id', 
            'name', 
            'company', 
            'employee_count',
            'created_by', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    def validate_company(self, value):
        # Ensure the company exists
        try:
            Company.objects.get(pk=value.id)
        except Company.DoesNotExist:
            raise serializers.ValidationError("Invalid company ID")
        return value