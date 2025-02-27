from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    days_employed = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ['id', 'company', 'department', 'status', 'name', 'email', 'mobile', 'address', 'designation', 'hired_on', 'days_employed']

    def validate(self, data):
        if data['department'].company != data['company']:
            raise serializers.ValidationError("Department must belong to the selected company.")
        return data