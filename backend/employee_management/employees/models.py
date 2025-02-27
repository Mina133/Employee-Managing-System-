from django.db import models
from companies.models import Company
from departments.models import Department
from django.utils import timezone

class Employee(models.Model):
    STATUS_CHOICES = (
        ('application_received', 'Application Received'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('hired', 'Hired'),
        ('not_accepted', 'Not Accepted'),
    )
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='application_received')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=50)
    hired_on = models.DateField(null=True, blank=True)

    @property
    def days_employed(self):
        if self.hired_on:
            return (timezone.now().date() - self.hired_on).days
        return 0

    def save(self, *args, **kwargs):
        # Ensure department belongs to the selected company
        if self.department.company != self.company:
            raise ValueError("Department must belong to the selected company.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name