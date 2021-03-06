from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('core/', include('core.urls')),
    path('partner/', include('partner.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
