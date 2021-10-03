from django.contrib import admin
from .models.customer_models import StripeCustomer
from .models.payment_models import StripePayment


class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = ["user", "stripe_customer_id", "created_at"]


class StripePaymentAdmin(admin.ModelAdmin):
    list_display = ["customer", "payment_intent_id"]


admin.site.register(StripeCustomer, StripeCustomerAdmin)
admin.site.register(StripePayment, StripePaymentAdmin)
