from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """Basic Question model.
    Question has many answers but only one or more of them can be true.
    """

    def __str__(self):
        return self.title

    title = models.CharField(max_length=512)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)


class Answer(models.Model):
    """Basic Answer model.
    This model has only the answer text and is_correct field from which admin can define if the
    Answer is correct or not.
    """

    def __str__(self) -> str:
        return self.answer

    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    answer = models.TextField()
    is_correct = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)


class Quiz(models.Model):
    """Base Quiz model. Staff member or some other subscription user will be able to create a new quiz."""

    def __str__(self):
        return self.title

    title = models.CharField(max_length=512)
    description = models.TextField()

    score = models.IntegerField(default=0)

    published = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    valid_from = models.DateTimeField(blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
