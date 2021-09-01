from django.urls import path
from .views import quiz, quiz_question

urlpatterns = [
    path("<int:id>/", quiz, name="index"),
    path("question/<int:id>/", quiz_question, name="quiz_question"),
]
