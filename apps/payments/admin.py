from django.contrib import admin
from .models.customer_models import StripeCustomer
from .models.payment_models import StripePayment


class StripeCustomerAdmin(admin.ModelAdmin):
    pass


class StripePaymentAdmin(admin.ModelAdmin):
    pass


admin.site.register(StripeCustomer, StripeCustomerAdmin)
admin.site.register(StripePayment, StripePaymentAdmin)
