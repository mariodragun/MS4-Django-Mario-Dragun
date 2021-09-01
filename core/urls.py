from django.urls import path
from .views import quiz, quiz_question, index

urlpatterns = [
    path("", index, name="index"),
    path("quiz/<int:id>/", quiz, name="quiz_start"),
    path("quiz/question/<int:id>/", quiz_question, name="quiz_question"),
]
