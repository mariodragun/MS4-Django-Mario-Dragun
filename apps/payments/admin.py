from django.contrib import admin
from .models.customer_models import StripeCustomer


class StripeCustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(StripeCustomer, StripeCustomerAdmin)
