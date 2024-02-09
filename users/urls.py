from django.views.generic import TemplateView

from users.apps import UsersConfig
from django.urls import path
from users.views import RegisterView, ProfileView, LoginView, LogoutView, forgot_password, EmailVerify
from django.contrib.auth import views as auth_views

app_name = 'users'




urlpatterns = [
    path("", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('forgot/', forgot_password, name='forgot'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('confirm_email/', TemplateView.as_view(template_name='users/confirm_email.html'), name='confirm_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='users/invalid_verify.html'), name='invalid_verify'),

]
