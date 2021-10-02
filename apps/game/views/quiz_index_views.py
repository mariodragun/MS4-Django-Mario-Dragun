from django.views.generic import ListView
from ..models.quiz_models import Quiz
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class QuizIndex(ListView):
    model = Quiz
    template_name = "game/quiz/quiz_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quizes"] = self.model.objects.all()
        return context
