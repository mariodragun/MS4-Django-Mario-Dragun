# Generated by Django 3.2.6 on 2021-08-29 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_quiztaken"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="answers", to="core.question"
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="questions", to="core.quiz"
            ),
        ),
        migrations.AlterField(
            model_name="quiztaken",
            name="quiz",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="user_quizes", to="core.quiz"
            ),
        ),
    ]
