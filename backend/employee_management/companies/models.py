# Create your models here.
from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_companies'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def num_departments(self):
        return self.departments.count()

    @property
    def num_employees(self):
        return self.employees.count()

    def __str__(self):
        return self.name