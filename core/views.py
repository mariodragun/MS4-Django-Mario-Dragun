from django import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz
from django.template import loader


def quiz(request, id):
    # load correct template
    template = loader.get_template("core/quiz.html")

    try:
        # try and find quiz object based on the provided `id`
        quiz_object = Quiz.objects.get(id=id, is_active=True)
        # define context to be sent to template
        context = {"quiz_object": quiz_object}
    except Exception:
        return HttpResponse("Quiz not found or not active")

    return HttpResponse(template.render(context, request))
