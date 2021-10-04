from django.views.generic import TemplateView


class AccountSettings(TemplateView):
    template_name = "accounts/settings.html"
