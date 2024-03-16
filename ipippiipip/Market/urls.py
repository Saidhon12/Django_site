from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('addadmin/', addadmin, name='addadmin'),
    path('log_admin/', log_admin, name='log_admin'),
]




















