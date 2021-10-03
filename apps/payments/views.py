from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import stripe
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

        return HttpResponse(status=200)


class PaymentSuccessView(TemplateView):
    template_name = "payments/success.html"
