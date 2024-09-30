from django.contrib import admin
from django.urls import path, include
from mozilla_django_oidc.views import OIDCAuthenticationCallbackView, OIDCAuthenticationRequestView

urlpatterns = [
    # path('oidc/login/', OIDCAuthenticationRequestView.as_view(), name='oidc_login'),
    # path('oidc/callback/', OIDCAuthenticationCallbackView.as_view(), name='oidc_callback'),
    path('admin/', admin.site.urls),
    path('api/', include('orders.urls')),
    path('users/', include('users.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('oidc/', include('mozilla_django_oidc.urls')),
]
