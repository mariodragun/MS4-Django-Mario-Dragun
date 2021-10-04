from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class PaymentSuccessView(TemplateView):
    template_name = "payments/success.html"
