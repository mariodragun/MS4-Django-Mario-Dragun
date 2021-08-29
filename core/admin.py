from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ["answer", "is_correct"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
