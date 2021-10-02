from django.shortcuts import redirect, render

from django.views.generic import FormView
from ..forms.register_forms import UserRegisterForm


class UserRegisterView(FormView):
    template_name = "authentication/register.html"
    form_class = UserRegisterForm
    success_url = "/auth/login"

    def post(self, request, *args, **kwargs):
        """Post method - will handle incoming POST request which will have all
        the form data.
        It will validate form information and if everything is good it will
        trigger .save() method which will create a new User in the database.
        """

        # get current form instance which is defined by the form_class
        form = self.get_form()

        if form.is_valid():
            # create new user with the appropriate data
            form.save()

            # redirect user on the login screen
            return redirect(self.success_url)

        else:
            # handling invalid form data (when validation fails)
            # will render the form again with the error information
            return render(self.request, self.template_name, context=self.get_context_data())
