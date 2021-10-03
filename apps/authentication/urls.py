from django.urls import path
from django.contrib.auth import views as auth_views
from .views.register_views import UserRegisterView

urlpatterns = [
    # use django authentication login view
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="authentication/login.html", redirect_authenticated_user=True),
        name="login",
    ),
    # use django authentaication logout view
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
]
