from django.urls import path
from . import views
app_name = 'hrms'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('register/', views.Register.as_view(), name='reg'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard')
]
