from django.db import models
import random
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
    thumb = models.ImageField(blank=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    department = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    joined = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.first_name

class AdminProfile(models.Model):
    thumb = models.ImageField(blank=True)