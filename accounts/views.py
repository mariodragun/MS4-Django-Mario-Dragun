from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def user_register(request):
    register_template = loader.get_template("accounts/register.html")

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
