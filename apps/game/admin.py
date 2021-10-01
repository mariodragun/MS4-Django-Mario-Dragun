from django.contrib import admin
from .models.question_models import Question
from .models.answer_models import Answer, SelectedAnswer
from .models.quiz_models import Quiz, QuizTaken


class AnswersInline(admin.TabularInline):
    """Admin inline tabular view to display and be able to easily create multiple Answers to the
    specific Question Admin view.
    """

    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    inlines = [
        AnswersInline,
    ]


class QuizAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "is_active"]


class QuizTakenAdmin(admin.ModelAdmin):
    list_display = ["user", "quiz", "status", "score"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizTaken, QuizTakenAdmin)
admin.site.register(SelectedAnswer)
