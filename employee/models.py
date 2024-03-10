from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=20, default='pending')  # pending, active, etc.
    admin_username = models.CharField(max_length=50, blank=True, null=True)
    admin_password = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username




class LeaveRequest(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=100)




