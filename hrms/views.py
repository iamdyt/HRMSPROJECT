from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,View,DetailView,TemplateView
from .forms import RegistrationForm,LoginForm

# Create your views here.
class Index(View):
    def get(self,request):
        return redirect('hrms:login')

class Register (CreateView):
    model = User
    form_class  = RegistrationForm
    template_name = 'hrmst/registrations/register.html'
    success_url = reverse_lazy('hrms:login')
    
class Login_View(LoginView):
    model = User
    form_class = LoginForm
    template_name = 'hrms/registrations/login.html'
    
class Dashboard(TemplateView):
    template_name = 'hrms/dashboard/index.html'
    