from django.db import models


class StripePayment(models.Model):
    """Stripe Payment model will store all the payments made by users."""

    def __str__(self):
        return str(self.customer) + " - " + str(self.payment_intent_id)

    customer = models.ForeignKey("StripeCustomer", on_delete=models.CASCADE)

    payment_intent_id = models.CharField(max_length=512)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
