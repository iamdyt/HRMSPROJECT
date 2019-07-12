from django.contrib import admin
from .models import Employee,Department,AdminProfile,Attendance
# Register your models here.
admin.site.register([Employee,Department,AdminProfile,Attendance])
