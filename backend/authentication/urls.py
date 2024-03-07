from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views.register import register
from .views.log_in import log_in, log_out
from .views.testauthor import testAuth


urlpatterns = [
    path('register', register),
    path('login', log_in),
    path('logout', log_out),
    path('testAuth', testAuth)
]