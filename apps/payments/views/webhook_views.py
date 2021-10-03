from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import stripe
from stripe.api_resources import customer, payment_intent
from quiz import settings
from ..models.customer_models import StripeCustomer
from ..models.payment_models import StripePayment


@method_decorator(csrf_exempt, name="dispatch")
class StripeWebhook(View):
    """View which will process incomming webhook information"""

    def _create_or_update_payment(self, event, payment_intent):
        """Create or Update payment object which is stored on our DB."""

        customer = StripeCustomer.objects.get(stripe_customer_id=event["data"]["object"]["customer"])
        _, _ = StripePayment.objects.update_or_create(customer=customer, payment_intent_id=payment_intent)

    def _get_payment_information(self, event):
        """Get Payment information from the Stripe, including charge id's."""

        stripe.api_key = settings.STRIPE_SECRET_KEY

        payment_intent_id = event["data"]["object"]["payment_intent"]
        payment_intent_stripe = stripe.PaymentIntent.retrieve(id=payment_intent_id)

        charges = payment_intent_stripe["charges"]
        charges_list = list()
        # get charge id's from the data list
        for item in charges["data"]:
            charges_list.append(item["id"])

        # return payment id
        return payment_intent_id

    def post(self, request):

        # get the stripe payload
        payload = request.body
        # get signature header from request meta
        signature_header = self.request.META["HTTP_STRIPE_SIGNATURE"]

        event = None

        # construct event to validate information recieved
        try:
            event = stripe.Webhook.construct_event(payload, signature_header, settings.STRIPE_WEBHOOK_SECRET)
        except stripe.error.SignatureVerificationError as e:
            return HttpResponse(status=400)

        # if event sent is checkout session complete use that information to store new user on our end.
        if event["type"] == "checkout.session.completed":
            # get payment intent from event
            payment_intent = self._get_payment_information(event=event)
            # create or update payment information on our DB
            self._create_or_update_payment(event=event, payment_intent=payment_intent)

        return HttpResponse(status=200)
