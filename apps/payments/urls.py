from django.urls import path
from .views import StripeWebhook


urlpatterns = [
    path("webhook/", StripeWebhook.as_view(), name="stripe_webhook"),
]
