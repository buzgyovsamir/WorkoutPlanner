from django.db import models

from exercises.migrations.choices import MuscleGroupChoices, DifficultyChoices


class Exercise(models.Model):
    name = models.CharField(
        max_length=100,
    )
    muscle_group = models.CharField(
        max_length=100,
        choices=MuscleGroupChoices.choices,
    )
    difficulty = models.CharField(
        max_length=20,
        choices=DifficultyChoices.choices,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name