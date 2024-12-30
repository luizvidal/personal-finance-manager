from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('', lambda request: redirect('login'))
]
