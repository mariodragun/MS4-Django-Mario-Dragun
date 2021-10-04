from django.urls.base import reverse
from django.views.generic import FormView
from django.shortcuts import redirect
from ..forms.change_password_forms import ChangePasswordForm


class UserPasswordChangeView(FormView):
    form_class = ChangePasswordForm

    def post(self, request):
        form = self.get_form()

        print(form.cleaned_data())

        return redirect(reverse("accounts:account_settings"))
