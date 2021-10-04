from django.views.generic import TemplateView


class AccountSettings(TemplateView):
    template_name = "accounts/settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        context["user"] = user

        return context
