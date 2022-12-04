from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=499)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeetName = models.CharField(max_length=499)
    Department = models.CharField(max_length=499)
    DateofJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=499)


