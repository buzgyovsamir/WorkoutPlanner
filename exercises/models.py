from django.db import models
from exercises.choices import ExerciseTypeChoices


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    exercise_type = models.CharField(
        max_length=20,
        choices=ExerciseTypeChoices.choices,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    suggested_min_reps = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )
    suggested_max_reps = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
