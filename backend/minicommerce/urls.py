from django.contrib import admin
from django.urls import path, include
from mozilla_django_oidc.views import OIDCAuthenticationCallbackView, OIDCAuthenticationRequestView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/orders/', include('orders.urls')),
    path('api/user/', include('users.urls')),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/oidc/', include('mozilla_django_oidc.urls')),
]
