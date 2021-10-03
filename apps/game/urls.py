from django.urls import path
from .views import GameIndexView
from .views.quiz_views import QuizGameView
from .views.quiz_question_views import QuizQuestionView
from .views.quiz_index_views import QuizIndexView

urlpatterns = [
    path("", GameIndexView.as_view(), name="index"),
    path("quiz/", QuizIndexView.as_view(), name="quiz_list_index"),
    path("quiz/<pk>/", QuizGameView.as_view(), name="quiz_start"),
    path("quiz/question/<pk>/", QuizQuestionView.as_view(), name="quiz_question"),
]
