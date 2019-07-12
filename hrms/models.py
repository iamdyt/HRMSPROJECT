from django.db import models
import random
from django.utils import timezone
import time
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    LANGUAGE = (('english','ENGLISH'),('yoruba','YORUBA'),('hausa','HAUSA'),('french','FRENCH'))
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    emp_id = models.CharField(max_length=70, unique=True, default='emp'+str(random.randrange(100,999,1)))
    thumb = models.ImageField(blank=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    emergency = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER, max_length=10)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now())
    language = models.CharField(choices=LANGUAGE, max_length=10, default='english')

    def __str__(self):
        return self.first_name

class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField(time.time())
    last_out = models.TimeField(time.time())
    status = models.CharField(choices=STATUS, max_length=15 )
    staff = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return 'Attendance -> '+str(self.date)

class AdminProfile(models.Model):
    thumb = models.ImageField(blank=True, default='avatar2.png')
    user = models.OneToOneField(User,on_delete=models.CASCADE, default=0)

    def __str__(self):
        return str(self.user)