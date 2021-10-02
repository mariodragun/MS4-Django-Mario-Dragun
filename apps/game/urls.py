from django.urls import path

from .views.quiz_views import QuizIndex, index, QuizGame, QuizQuestion

urlpatterns = [
    path("", index, name="index"),
    path("quiz", QuizIndex.as_view(), name="quiz_list_index"),
    path("quiz/<pk>/", QuizGame.as_view(), name="quiz_start"),
    path("quiz/question/<pk>/", QuizQuestion.as_view(), name="quiz_question"),
]
