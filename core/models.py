from django.db import models


class Question(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=512)
    description = models.TextField()
    image = models.ImageField()
