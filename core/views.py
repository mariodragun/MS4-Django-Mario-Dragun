from django.shortcuts import render
from django.http import HttpResponse


def quiz(request):
    html = "<html><body>This is a placeholder for quiz</body></html>"
    return HttpResponse(html)
