from django.urls import path
from .views import quiz, quiz_question, index

urlpatterns = [
    path("", index, name="index"),
    path("<int:id>/", quiz, name="index"),
    path("question/<int:id>/", quiz_question, name="quiz_question"),
]
