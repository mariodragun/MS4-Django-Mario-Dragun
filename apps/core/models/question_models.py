from django.db import models


class Question(models.Model):
    """Basic Question model.
    Question has many answers but only one or more of them can be true.
    """

    def __str__(self):
        return self.title

    title = models.CharField(max_length=512)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, related_name="questions")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
