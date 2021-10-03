from django.views.generic import DetailView
from ..models.quiz_models import Quiz, QuizTaken
from ..models.question_models import Question
from ..models.answer_models import SelectedAnswer
from django.shortcuts import render
from django.utils import timezone


class QuizStatus:
    def __init__(self, quiz_taken) -> None:
        self._quiz_taken = quiz_taken

    def is_started(self):
        """Method to check if user has already started this particular quiz."""

        quiz_already_started = False
        # check if quiz is already started - if it is then set up already_started bool
        quiz_taken = self._quiz_taken

        if quiz_taken:
            quiz_already_started = True

        return quiz_already_started

    def is_completed(self, questions_list):
        """Method to check if all the questions had been answered in the quiz."""

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


class GameQuiz:
    def __init__(self, user, quiz):
        self._user = user
        self._quiz = quiz

    def _get_quiz_taken(self):
        """Method to return taken quiz for this user"""

        quiz_taken = QuizTaken.objects.filter(user=self._user, quiz=self._quiz)
        return quiz_taken

    def start(self):
        """Method to start a new quiz for the user, it will create an entry in the QuizTaken model."""

        # start quiz for this user - create a QuizTaken object or update
        quiz_taken, created = QuizTaken.objects.update_or_create(
            user=self._user,
            quiz=self._quiz,
            defaults={
                "status": QuizTaken.STATUS_STARTED,
            },
        )
        # check if object is created, if created set started_at at now()
        if created:
            quiz_taken.started_at = timezone.now()
            quiz_taken.save()

        return True

    def restart(self):
        """Method to restart quiz."""

        quiz_taken = self._get_quiz_taken()
        questions = Question.objects.filter(quiz=self._quiz)
        for question in questions:
            selected_answer = SelectedAnswer.objects.filter(user=self._user, quiz=self._quiz, question=question)
            selected_answer.delete()
        quiz_taken.delete()

        return self._get_quiz_taken()

    @property
    def status(self):
        """Property which will return QuizStatus object on the output, from which we can extract is_started and
        is_completed methods.
        """

        status = QuizStatus(quiz_taken=self._get_quiz_taken())
        return status


class QuizGameView(DetailView):
    model = Quiz
    template_name = "game/quiz.html"

    def _get_selected_answer(self, question, quiz):
        """Function to get all the selected answers for question and quiz."""

        selected_answer = SelectedAnswer.objects.filter(user=self.request.user, quiz=quiz, question=question).first()

        return selected_answer

    def _get_questions_list(self, quiz):
        """Function to get all the questions/answers and few additional variables."""

        questions_list = list()
        # iterate through quiz questions
        for question in quiz.questions.all():
            selected_answer = self._get_selected_answer(question=question, quiz=quiz)

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

    def get(self, request, pk):
        quiz = None
        try:
            # get quiz object
            quiz = self.model.objects.get(id=pk, is_active=True)
        except Exception:
            return render(self.request, template_name="common/errors/http_404.html", context={})

        # return 404 if there is no quiz object for the particular id
        if quiz:
            # game quiz
            quiz_game = GameQuiz(user=self.request.user, quiz=quiz)

            # check if quiz is started
            quiz_started = quiz_game.status.is_started()

            if self.request.GET.get("option") and self.request.GET["option"] == "start":
                # start new quiz
                quiz_started = quiz_game.start()
            elif self.request.GET.get("option") and self.request.GET["option"] == "restart":
                # delete old quiz for the user and start a new one
                quiz_started = quiz_game.restart()

            questions_list = self._get_questions_list(quiz=quiz)
            quiz_completed, answered_correctly_count = quiz_game.status.is_completed(questions_list=questions_list)

            # if quiz is completed render completed template
            if quiz_completed:
                context = {
                    "quiz": quiz,
                    "answered_correctly_count": answered_correctly_count,
                    "questions_count": len(questions_list),
                }

                return render(self.request, template_name="game/quiz/quiz_completed.html", context=context)

            # define context to be sent to template
            context = {
                "quiz_object": quiz,
                "questions_list": questions_list,
                "started": quiz_started,
                "quiz_completed": False,
            }
            return render(self.request, template_name=self.template_name, context=context)

        return render(self.request, template_name="common/errors/http_404.html", context={})
