from django.db import models


class ProgramGoalChoices(models.TextChoices):
    STRENGTH = "strength", "Strength"
    HYPERTROPHY = "hypertrophy", "Hypertrophy"


class ProgramLevelChoices(models.TextChoices):
    BEGINNER = "beginner", "Beginner"
    INTERMEDIATE = "intermediate", "Intermediate"
    ADVANCED = "advanced", "Advanced"
