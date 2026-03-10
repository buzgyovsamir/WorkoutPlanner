from django.db import models


class ProgramGoalChoices(models.TextChoices):
    STRENGTH = "STRENGTH", "Strength"
    MUSCLE_GAIN = "MUSCLE_GAIN", "Muscle Gain"
    FAT_LOSS = "FAT_LOSS", "Fat Loss"
    ENDURANCE = "ENDURANCE", "Endurance"
    GENERAL_FITNESS = "GENERAL_FITNESS", "General Fitness"


class ProgramLevelChoices(models.TextChoices):
    BEGINNER = "BEGINNER", "Beginner"
    INTERMEDIATE = "INTERMEDIATE", "Intermediate"
    ADVANCED = "ADVANCED", "Advanced"