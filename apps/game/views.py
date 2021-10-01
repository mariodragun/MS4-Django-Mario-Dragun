from django.http import HttpResponse, HttpResponseRedirect
from .models.quiz_models import Quiz, QuizTaken
from .models.question_models import Question
from .models.answer_models import SelectedAnswer
from django.shortcuts import get_object_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse


def index(request):
    """Basic index view."""

    # load template
    template = loader.get_template("game/index.html")
    context = {}

    # return response along with rendered template
    return HttpResponse(template.render(context, request))


@login_required()
def quiz_list_index(request):
    """View for quiz index view - it should present a list of quizes."""

    # get all quiz objects
    quizes = Quiz.objects.all()

    # load templates
    quiz_index_template = loader.get_template("game/quiz/quiz_list.html")

    # set basic context
    context = {"quizes": quizes}

    # if there are no quizes - return empty page with appropriate messages
    if not quizes:
        context["error_message"] = "There are no quizes at this time. Please wait until we approve them."

    return HttpResponse(quiz_index_template.render(context, request))


@login_required()
def quiz(request, id):
    # load correct template
    template = loader.get_template("game/quiz.html")

    def _quiz_taken(quiz):
        """Fuction to return taken quiz for this user"""

        quiz_taken = QuizTaken.objects.filter(user=request.user, quiz=quiz)
        return quiz_taken

    def _check_if_quiz_is_started(quiz):
        """Function to check if user has already started this particular quiz."""

        quiz_already_started = False
        # check if quiz is already started - if it is then set up already_started bool
        quiz_taken = _quiz_taken(quiz=quiz)

        if quiz_taken:
            quiz_already_started = True

        return quiz_already_started

    def _start_quiz(quiz):
        """Function to start a new quiz for the user, it will create an entry in the QuizTaken model."""

        # start quiz for this user - create a QuizTaken object or update
        quiz_taken, created = QuizTaken.objects.update_or_create(
            user=request.user,
            quiz=quiz,
            defaults={
                "status": QuizTaken.STATUS_STARTED,
            },
        )
        # check if object is created, if created set started_at at now()
        if created:
            quiz_taken.started_at = timezone.now()
            quiz_taken.save()

        return True

    def _get_selected_answer(question, quiz):
        """Function to get all the selected answers for question and quiz."""

        selected_answer = SelectedAnswer.objects.filter(user=request.user, quiz=quiz, question=question).first()

        return selected_answer

    def _reset_quiz(quiz):
        """Function to restart quiz."""

        quiz_taken = _quiz_taken(quiz=quiz)
        questions = Question.objects.filter(quiz=quiz)
        for question in questions:
            selected_answer = SelectedAnswer.objects.filter(user=request.user, quiz=quiz, question=question)
            selected_answer.delete()
        quiz_taken.delete()

        return _start_quiz(quiz=quiz)

    def _get_questions_list(quiz):
        """Function to get all the questions/answers and few additional variables."""

        questions_list = list()
        # iterate through quiz questions
        for question in quiz.questions.all():
            selected_answer = _get_selected_answer(question=question, quiz=quiz)

            answer_is_correct = False
            # if there is selected answer - check if that answer is correct
            if selected_answer:
                correct_answer = question.answers.filter(is_correct=True).first()
                if correct_answer and correct_answer.answer == selected_answer.content:
                    answer_is_correct = True

            # prepare all the required data
            data = {
                "question": question,
                "answers": question.answers.all(),
                "selected_answer_for_this_question": selected_answer,
                "answer_is_correct": answer_is_correct,
            }
            # append data to list
            questions_list.append(data)

        return questions_list

    def _is_quiz_completed(questions_list):
        """Function to check if all the questions had been answered in the quiz."""

        answered_qustions = 0
        correct_answers = 0
        # iterate through all of the questions
        for item in questions_list:
            if item.get("selected_answer_for_this_question"):
                answered_qustions += 1
            if item.get("answer_is_correct"):
                correct_answers += 1
        # compare counters
        if len(questions_list) == answered_qustions:
            return True, correct_answers
        return False, correct_answers

    try:
        # try and find quiz object based on the provided `id`
        quiz_object = Quiz.objects.get(id=id, is_active=True)

        # check if quiz started
        quiz_started = _check_if_quiz_is_started(quiz=quiz_object)

        if request.GET.get("option") and request.GET["option"] == "start":
            # start new quiz
            quiz_started = _start_quiz(quiz=quiz_object)
        elif request.GET.get("option") and request.GET["option"] == "restart":
            # delete old quiz for the user and start a new one
            quiz_started = _reset_quiz(quiz=quiz_object)

        questions_list = _get_questions_list(quiz=quiz_object)
        quiz_completed, answered_correctly_count = _is_quiz_completed(questions_list=questions_list)

        # if quiz is completed render completed template
        if quiz_completed:
            finish_template = loader.get_template("game/quiz/quiz_completed.html")
            context = {
                "quiz": quiz_object,
                "answered_correctly_count": answered_correctly_count,
                "questions_count": len(questions_list),
            }
            return HttpResponse(finish_template.render(context, request))

        # define context to be sent to template
        context = {
            "quiz_object": quiz_object,
            "questions_list": questions_list,
            "started": quiz_started,
            "quiz_completed": False,
        }
    except Exception:
        # display exception error
        error_template = loader.get_template("common/errors/http_404.html")
        context = {}
        # return response along with error template
        return HttpResponse(error_template.render(context, request))

    return HttpResponse(template.render(context, request))


@login_required()
def quiz_question(request, id):
    """View to store answer."""

    question = get_object_or_404(Question, pk=id)

    quiz_id = request.POST["quiz"]
    quiz = Quiz.objects.get(pk=quiz_id)

    choice_id = request.POST.get("choice")
    user = request.user

    # if there is no choice redirect back to quiz start
    if not choice_id:
        return HttpResponseRedirect(reverse("quiz:quiz_start", args=(quiz.id,)))

    try:
        selected_answer_choice = question.answers.get(id=choice_id)
    except Exception:
        pass

    if selected_answer_choice and quiz and user:
        # create new Selecte Answer or update existing one, if it is the Answer to the same Question
        ob, created = SelectedAnswer.objects.update_or_create(
            user=user,
            quiz=quiz,
            question=question,
            defaults={
                "content": selected_answer_choice.answer,
            },
        )

    # return redirect response to the quiz
    return HttpResponseRedirect(reverse("quiz:quiz_start", args=(quiz.id,)))
