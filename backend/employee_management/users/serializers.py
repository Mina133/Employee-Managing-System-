from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Include only fields that exist in your CustomUser model
        read_only_fields = ['id']  # Fields that cannot be modified