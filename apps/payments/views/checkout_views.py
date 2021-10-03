from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import stripe
from quiz import settings
from ..models.customer_models import StripeCustomer


@method_decorator(csrf_exempt, name="dispatch")
class CheckoutSession(TemplateView):
    template_name = "payments/checkout.html"

    def _get_or_create_customer(self, user):
        """Get or create stripe customer, if there is already a stripe customer in our DB
        which belongs to the current user, it will return it's customer ID.
        If Customer is not found in our DB it will create a new one, first on Stripe side,
        and after that in our DB.
        """

        stripe.api_key = settings.STRIPE_SECRET_KEY

        # check if this user is in our database
        customer = StripeCustomer.objects.filter(user=user).first()
        if customer:
            # return customer id
            return customer.stripe_customer_id

        # create a new customer on stripe side
        customer = stripe.Customer.create(email=self.request.user.email)

        # store new customer in the database
        try:
            StripeCustomer.objects.create(user=self.request.user, stripe_customer_id=customer["id"])
        except Exception:
            pass

        # return customer id
        return customer["id"]

    def post(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        donation_price_id = "price_1JfkQwHvCdKeKxUHteKKayOk"

        # get customer id
        customer_id = self._get_or_create_customer(user=self.request.user)

        # create checkout session
        checkout_session = stripe.checkout.Session.create(
            customer=customer_id,
            payment_method_types=["card"],
            line_items=[
                {
                    "price": donation_price_id,
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=settings.BASE_URL + "/payments/success/",
            cancel_url=settings.BASE_URL + "/payments/cancel/",
        )

        # return redirect to the session  url (it will redirect to Stripe side)
        return redirect(checkout_session.url)
