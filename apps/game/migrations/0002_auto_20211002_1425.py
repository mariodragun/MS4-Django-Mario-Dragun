# Generated by Django 3.2.6 on 2021-10-02 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizes'},
        ),
        migrations.AlterModelOptions(
            name='quiztaken',
            options={'verbose_name_plural': 'Quizes Taken'},
        ),
    ]
