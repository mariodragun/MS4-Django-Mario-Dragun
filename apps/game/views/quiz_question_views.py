from django.urls.base import reverse
from django.views.generic import DetailView
from ..models.quiz_models import Quiz
from ..models.question_models import Question
from ..models.answer_models import SelectedAnswer
from django.shortcuts import redirect


class QuizQuestionView(DetailView):
    model = Question

    def post(self, request, pk):
        # get question object based on the id
        question = self.model.objects.get(id=pk)

        # get quiz id from the fields in the form
        quiz_id = self.request.POST["quiz"]
        quiz = Quiz.objects.get(id=quiz_id)

        # get choice_id from the values on the form
        choice_id = self.request.POST.get("choice")
        user = request.user

        selected_answer_choice = None

        # if there is no choice redirect back to quiz start
        if not choice_id:
            return redirect(reverse("quiz:quiz_start", args=(quiz.id,)))

        # try to get selected answer choice
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
        return redirect(reverse("quiz:quiz_start", args=(quiz.id,)))
