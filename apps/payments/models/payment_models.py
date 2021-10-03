from django.db import models


class StripePayment(models.Model):
    """Stripe Payment model will store all the payments made by users."""

    customer = models.ForeignKey("StripeCustomer", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
