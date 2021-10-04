from django.urls.base import reverse
from django.views.generic import FormView
from django.shortcuts import redirect
from ..forms.change_password_forms import ChangePasswordForm
from ..forms.basic_user_information_forms import BasicUserInformationForm


class UserPasswordChangeView(FormView):
    form_class = ChangePasswordForm

    def post(self, request):
        form = self.get_form()

        print(form.cleaned_data())

        return redirect(reverse("accounts:account_settings"))


class UserBasicInformationChangeView(FormView):
    form_class = BasicUserInformationForm

    def post(self, request):
        form = BasicUserInformationForm(request.POST)
        if form.is_valid():
            print("it is valid")
            print(form.cleaned_data)

        print(form.errors)
        return redirect(reverse("accounts:account_settings"))
