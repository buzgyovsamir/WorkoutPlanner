from django.db import models
from django.core.exceptions import ValidationError
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

    def clean(self):
        if self.name:
            self.name = self.name.strip()

        if len(self.name) < 3:
            raise ValidationError(
                {"name": "Program name must be at least 3 characters long."}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
