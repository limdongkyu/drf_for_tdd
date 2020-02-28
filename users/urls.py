from django.urls import path

from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutView

app_name = 'users'

urlpatterns = [
    path('users', UserRegistrationAPIView.as_view(), name="list"),
    path('users/login', UserLoginAPIView.as_view(), name="login"),
    path('users/logout', UserLogoutView.as_view(), name="logout"),
]
