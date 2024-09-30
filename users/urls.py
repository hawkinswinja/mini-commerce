from django.urls import path
from . import views

urlpatterns = [   
    path('login_error/', views.login_error, name='login_error'),
]