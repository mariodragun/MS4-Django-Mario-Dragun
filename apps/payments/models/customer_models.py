from django.db import models
from django.contrib.auth.models import User


class StripeCustomer(models.Model):
    """Customer model which will store Stripe Customer id's connected to the
    quiz users itself.
    """

    def __str__(self) -> str:
        return str(self.user) + " - " + str(self.stripe_customer_id)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=512)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
