from django.urls import path
from .views.checkout_views import CheckoutSession
from .views.success_views import PaymentSuccessView
from .views.webhook_views import StripeWebhook


urlpatterns = [
    path("webhook/", StripeWebhook.as_view(), name="stripe_webhook"),
    path("success/", PaymentSuccessView.as_view(), name="success"),
    path("checkout/", CheckoutSession.as_view(), name="stripe_checkout"),
]
