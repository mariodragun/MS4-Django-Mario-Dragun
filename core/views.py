from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz


def quiz(request, id):

    try:
        quiz_object = Quiz.objects.get(id=id, is_active=True)
    except Exception:
        return HttpResponse("Quiz not found or not active")
    return HttpResponse("Quiz found - not rendering it yet")
