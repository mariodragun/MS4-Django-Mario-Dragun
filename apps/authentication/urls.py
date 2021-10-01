from django.urls import path
from django.contrib.auth import views as auth_views
from .views.register_views import user_register

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="authentication/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", user_register, name="register"),
]
