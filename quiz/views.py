from django.shortcuts import render


# Defining custom 404 page which will be displayed when DEBUG is set to False (Production environment)
def error_404(request, exception):
    return render(request, "common/errors/http_404.html", status=404)
