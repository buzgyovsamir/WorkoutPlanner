from django.db import models
from programs.choices import ProgramGoalChoices, ProgramLevelChoices


class Program(models.Model):
    name = models.CharField(
        max_length=100,
    )
    goal = models.CharField(
        max_length=100,
        choices=ProgramGoalChoices.choices,
    )
    level = models.CharField(
        max_length=100,
        choices=ProgramLevelChoices.choices,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
