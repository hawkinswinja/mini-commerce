from django.urls import path
from . import views

urlpatterns = [   
    path('isauthenticated/', views.check_authentication),
    path('csrf/', views.get_csrf),
    path('login/', views.LoginView.as_view()),
]