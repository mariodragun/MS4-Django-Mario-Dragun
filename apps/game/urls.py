from django.urls import path
from .views import GameIndex
from .views.quiz_views import QuizIndex, QuizGame, QuizQuestion

urlpatterns = [
    path("", GameIndex.as_view(), name="index"),
    path("quiz", QuizIndex.as_view(), name="quiz_list_index"),
    path("quiz/<pk>/", QuizGame.as_view(), name="quiz_start"),
    path("quiz/question/<pk>/", QuizQuestion.as_view(), name="quiz_question"),
]
