from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path("settings/", , name="settings"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("reset-password/", auth_views.PasswordChangeView.as_view(), name="reset_password"),
]
