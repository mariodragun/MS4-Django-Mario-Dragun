from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    """Basic Answer model.
    This model has only the answer text and is_correct field from which admin can define if the
    Answer is correct or not.
    """

    def __str__(self) -> str:
        return self.answer

    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="answers")
    answer = models.TextField()
    is_correct = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)


class SelectedAnswer(models.Model):
    """Model for storing users answers based on the question and the quiz
    itslef.
    """

    def __str__(self):
        return self.content

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)

    content = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
