from django.views.generic import ListView
from ..models.quiz_models import Quiz
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class QuizIndexView(ListView):
    model = Quiz
    template_name = "game/quiz/quiz_list.html"

    def get_context_data(self, **kwargs):
        # get base context
        context = super().get_context_data(**kwargs)

        # get all of the quiz objects
        quizes = self.model.objects.all()

        # if there are quiz objects return all of them, otherwise send error message
        if quizes:
            context["quizes"] = self.model.objects.all()
        else:
            context[
                "error_message"
            ] = "There are no quizes at this moment. Please wait until new ones are created or approved."

        # return context
        return context
