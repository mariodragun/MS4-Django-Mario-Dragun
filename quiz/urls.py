"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("apps.game.urls", "apps.game"), namespace="quiz")),
    path("accounts/", include(("apps.accounts.urls", "apps.accounts"), namespace="accounts")),
    path("auth/", include(("apps.authentication.urls", "apps.authentication"), namespace="authentication")),
    path("payments/", include(("apps.payments.urls", "apps.payments"), namespace="payments")),
]

# custom 404 page handler
handler404 = "quiz.views.error_404"
