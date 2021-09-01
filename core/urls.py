from django.urls import path
from .views import quiz

urlpatterns = [
    path("<int:id>/", quiz, name="index"),
]
