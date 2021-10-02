from django.http.response import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from django.views.generic import TemplateView, FormView
from ..forms.register_forms import UserRegisterForm

from django.contrib.auth.models import User


def user_register(request):
    register_template = loader.get_template("authentication/register.html")

    error_message = None

    if request.method == "POST":
        username = request.POST["req-username-input"]
        password = request.POST["req-password-input"]
        repeat_password = request.POST["req-re-password-input"]

        if password != repeat_password:
            error_message = "Missmatch in the password. Both passwords need to be the same"

            context = {"error_message": error_message}
            return HttpResponse(register_template.render(context, request))

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("quiz:index")

    context = {"error_message": error_message}
    return HttpResponse(register_template.render(context, request))


class UserRegisterView(FormView):
    template_name = "authentication/register.html"
    form_class = UserRegisterForm
    success_url = "/auth/login"

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            context = {"error_message": "All is good", "form": form}

            # create new user with the appropriate data
            form.save()

            # redirect user on the login screen
            return HttpResponseRedirect(redirect_to=self.success_url)
        else:
            print(form.errors)

            context = {"error_message": "Feck", "form": form}
            return render(self.request, self.template_name, context)
