from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('demo-login/', views.demo_login, name='demo_login'),

    path('', views.students, name='students'),
]
