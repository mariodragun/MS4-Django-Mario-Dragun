# Generated by Django 3.2.6 on 2021-08-28 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0006_question_quiz"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuizTaken",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "status",
                    models.CharField(
                        choices=[("STARTED", "Started"), ("PAUSED", "Paused"), ("FINISHED", "Finished")],
                        default="STARTED",
                        max_length=256,
                    ),
                ),
                ("score", models.IntegerField(default=0)),
                ("started_at", models.DateTimeField(blank=True, null=True)),
                ("finished_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("quiz", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="core.quiz")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
