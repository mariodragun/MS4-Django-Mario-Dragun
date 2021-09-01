from django.http import HttpResponse
from .models import Answer, Quiz, Question, SelectedAnswer
from django.shortcuts import get_object_or_404, render
from django.template import loader


def index(request):
    """Basic index view."""

    # load template
    template = loader.get_template("core/base.html")
    context = {}

    # return response along with rendered template
    return HttpResponse(template.render(context, request))


def quiz(request, id):
    # load correct template
    template = loader.get_template("core/quiz.html")

    try:
        # try and find quiz object based on the provided `id`
        quiz_object = Quiz.objects.get(id=id, is_active=True)
        # define context to be sent to template
        context = {"quiz_object": quiz_object, "questions": quiz_object.questions.all()}
    except Exception:
        return HttpResponse("Quiz not found or not active")

    return HttpResponse(template.render(context, request))


def quiz_question(request, id):
    """View to store answer."""

    question = get_object_or_404(Question, pk=id)

    quiz_id = request.POST["quiz"]
    choice_id = request.POST["choice"]
    user = request.user

    quiz = None

    try:
        selected_answer_choice = question.answers.get(id=choice_id)
        quiz = Quiz.objects.get(pk=quiz_id)
    except Exception as e:
        pass

    if selected_answer_choice and quiz and user:
        ob, created = SelectedAnswer.objects.update_or_create(
            user=user,
            quiz=quiz,
            question=question,
            defaults={
                "content": selected_answer_choice.answer,
            },
        )

        return HttpResponse("Answer is stored")

    return HttpResponse("Something happened")
