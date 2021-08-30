from django.contrib import admin
from .models import Question, Answer


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


admin.site.register(Question, QuestionAdmin)
