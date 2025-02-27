from django.contrib import admin

# Register your models here.
from .models import CustomUser
from companies.models import Company
from departments.models import Department
from employees.models import Employee

admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Employee)