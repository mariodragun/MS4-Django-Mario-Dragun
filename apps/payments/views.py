from django.shortcuts import redirect, render
from django.views.generic import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import stripe
from stripe.api_resources import line_item, payment_method
from quiz import settings


# Webhook
@method_decorator(csrf_exempt, name="dispatch")
class StripeWebhook(View):
    """View which will process incomming webhook information"""

    def post(self, request):
        # get the stripe payload
        payload = request.body
        signature_header = self.request.META["HTTP_STRIPE_SIGNATURE"]

        event = None

        try:
            event = stripe.Webhook.construct_event(payload, signature_header, settings.STRIPE_WEBHOOK_SECRET)
        except stripe.error.SignatureVerificationError as e:
            return HttpResponse(status=400)

        if event["type"] == "checkout.session.completed":
            print("Payment was successful.")

        if event["type"] == "charge.succeeded":
            # process this charge information to get all the necesarry information
            pass

        return HttpResponse(status=200)


class PaymentSuccessView(TemplateView):
    template_name = "payments/success.html"


class CheckoutSession(View):
    def post(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        donation_price_id = "price_1JfkQwHvCdKeKxUHteKKayOk"

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": donation_price_id,
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=settings.BASE_URL + "/payments/success.html",
            cancel_url=settings.BASE_URL + "/payments/cancel.html",
        )

        return redirect(checkout_session.url)
