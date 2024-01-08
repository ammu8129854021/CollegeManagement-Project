from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    joining_date = models.DateField()
    qualification = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
