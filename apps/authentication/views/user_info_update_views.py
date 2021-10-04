from django.urls.base import reverse
from django.views.generic import FormView
from django.shortcuts import redirect, render
from ..forms.change_password_forms import ChangePasswordForm
from ..forms.basic_user_information_forms import BasicUserInformationForm


class UserPasswordChangeView(FormView):
    form_class = ChangePasswordForm

    def post(self, request):
        form = self.get_form()

        if form.is_valid():

            # get user
            user = self.request.user

            # update user information
            form.save(user=user)

        # redirect to accounts page
        return redirect(reverse("accounts:account_settings"))


class UserBasicInformationChangeView(FormView):
    form_class = BasicUserInformationForm

    def post(self, request):
        form = self.get_form()
        if form.is_valid():

            # get user
            user = self.request.user

            # update user information
            form.save(user=user)

        # redirect to the accounts page
        return redirect(reverse("accounts:account_settings"))
