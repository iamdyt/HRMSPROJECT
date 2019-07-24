from .models import Department

def get_departments(request):

    depts = Department.objects.all().order_by('name')
    return { 'depts':depts}