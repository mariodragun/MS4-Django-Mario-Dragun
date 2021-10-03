from django.urls import path
from .views import StripeWebhook, PaymentSuccessView


urlpatterns = [
    path("webhook/", StripeWebhook.as_view(), name="stripe_webhook"),
    path("success/", PaymentSuccessView.as_view(), name="success"),
]
