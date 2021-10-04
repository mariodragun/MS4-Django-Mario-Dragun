from django.urls import path
from .views.settings_views import AccountSettings


urlpatterns = [
    path("settings/", AccountSettings.as_view(), name="account_settings"),
]
