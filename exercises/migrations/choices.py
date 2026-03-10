from django.db import models

class MuscleGroupChoices(models.TextChoices):
    CHEST = "CHEST", "Chest"
    BACK = "BACK", "Back"
    LEGS = "LEGS", "Legs"
    SHOULDERS = "SHOULDERS", "Shoulders"
    ARMS = "ARMS", "Arms"
    CORE = "CORE", "Core"


class DifficultyChoices(models.TextChoices):
    BEGINNER = "BEGINNER", "Beginner"
    INTERMEDIATE = "INTERMEDIATE", "Intermediate"
    ADVANCED = "ADVANCED", "Advanced"