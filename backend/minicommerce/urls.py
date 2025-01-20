from django.contrib import admin
from django.urls import path, include
from mozilla_django_oidc.views import OIDCAuthenticationCallbackView, OIDCAuthenticationRequestView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
    path('user/', include('users.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('oidc/', include('mozilla_django_oidc.urls')),
]
