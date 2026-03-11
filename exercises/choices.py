from django.db import models


class ExerciseTypeChoices(models.TextChoices):
    COMPOUND = "compound", "Compound"
    HYPERTROPHY = "hypertrophy", "Hypertrophy"
