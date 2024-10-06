from django.urls import path
from . import views

urlpatterns = [
    path('isauthenticated/', views.check_authentication, name='is_authenticated'),
    path('csrf/', views.get_csrf, name='get_csrf'),
    path('login/', views.LoginView.as_view(), name='user_login'),
]
