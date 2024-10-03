from django.urls import path
from . import views

urlpatterns = [   
    path('isauthenticated/', views.check_authentication),
    path('login/', views.LoginView.as_view()),
]