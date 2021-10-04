from django.views.generic import TemplateView
from apps.authentication.forms.change_password_forms import ChangePasswordForm
from apps.authentication.forms.basic_user_information_forms import BasicUserInformationForm


class AccountSettings(TemplateView):
    template_name = "accounts/settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get user from the request
        user = self.request.user

        # set user in the context
        context["user"] = user

        # set change password form in the context
        context["change_password_form"] = ChangePasswordForm()

        # prefil basic user information with the data which we have in the DB, and add it into context
        context["basic_user_information_form"] = BasicUserInformationForm(
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
        )

        # return context
        return context
