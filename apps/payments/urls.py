from django.urls import path
from .views import StripeWebhook, PaymentSuccessView, CheckoutSession


urlpatterns = [
    path("webhook/", StripeWebhook.as_view(), name="stripe_webhook"),
    path("success/", PaymentSuccessView.as_view(), name="success"),
    path("checkout/", CheckoutSession.as_view(), name="stripe_checkout"),
]
