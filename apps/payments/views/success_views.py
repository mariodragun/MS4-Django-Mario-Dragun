from django.views.generic import TemplateView


class PaymentSuccessView(TemplateView):
    template_name = "payments/success.html"
