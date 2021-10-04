from django.urls.base import reverse
from django.views.generic import FormView
from django.shortcuts import redirect, render
from ..forms.change_password_forms import ChangePasswordForm
from ..forms.basic_user_information_forms import BasicUserInformationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class UserPasswordChangeView(FormView):
    form_class = ChangePasswordForm

    def post(self, request):
        form = self.get_form()

        if form.is_valid():

            # get user
            user = self.request.user

            # update user information
            form.save(user=user)
            messages.success(request, "Password changed successfully.")
            return redirect(reverse("accounts:account_settings"))

        # redirect to accounts page
        messages.error(
            request,
            "Something went wrong. Could not change password, make sure that both password fields have same value.",
        )
        return redirect(reverse("accounts:account_settings"))


@method_decorator(login_required, name="dispatch")
class UserBasicInformationChangeView(FormView):
    form_class = BasicUserInformationForm

    def post(self, request):
        form = self.get_form()
        if form.is_valid():

            # get user
            user = self.request.user

            # update user information
            form.save(user=user)
            messages.success(request, "Basic Information updated.")
            return redirect(reverse("accounts:account_settings"))

        # redirect to the accounts page
        messages.error(request, "Something went wrong. Could not update basic user information.")
        return redirect(reverse("accounts:account_settings"))
