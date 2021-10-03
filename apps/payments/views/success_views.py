from django.views.generic import View, TemplateView


class PaymentSuccessView(TemplateView):
    template_name = "payments/success.html"
