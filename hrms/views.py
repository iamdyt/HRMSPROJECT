from django.shortcuts import render,redirect, resolve_url
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models  import AdminProfile,Employee, Department
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,View,DetailView,TemplateView,ListView
from .forms import RegistrationForm,LoginForm
from django.contrib import messages

# Create your views here.
class Index(View):
    def get(self,request):
        return redirect('hrms:login')

class Register (CreateView):
    model = User
    form_class  = RegistrationForm
    template_name = 'hrms/registrations/register.html'
    success_url = reverse_lazy('hrms:login')
    
class Login_View(LoginView):
    model = User
    form_class = LoginForm
    template_name = 'hrms/registrations/login.html'

    def get_success_url(self):
        query = User.objects.get(adminprofile__user=self.request.user.pk)
        self.request.session['auth_user'] = query.username
        self.request.session['auth_user_thumb'] = query.adminprofile.thumb.url
        url = reverse_lazy('hrms:dashboard')
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)
    
    
class Dashboard(LoginRequiredMixin,ListView):
    template_name = 'hrms/dashboard/index.html'
    login_url = 'hrms:login'
    model = User
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        return context

#### EMPLOYEE'S CONTROLLER START HERE
class Employee_All(ListView):
    template_name = 'hrms/employee/index.html'
    model = Employee
    context_object_name = 'employees'
### STOPS HERE
    
    