from django.urls import path
from .views import GameIndex
from .views.quiz_views import QuizGame
from .views.quiz_question_views import QuizQuestion
from .views.quiz_index_views import QuizIndex

urlpatterns = [
    path("", GameIndex.as_view(), name="index"),
    path("quiz", QuizIndex.as_view(), name="quiz_list_index"),
    path("quiz/<pk>/", QuizGame.as_view(), name="quiz_start"),
    path("quiz/question/<pk>/", QuizQuestion.as_view(), name="quiz_question"),
]
