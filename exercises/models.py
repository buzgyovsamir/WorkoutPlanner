from django.db import models
from django.core.exceptions import ValidationError
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

    def clean(self):
        if self.name:
            self.name = self.name.strip()

        errors = {}

        if len(self.name) < 3:
            errors["name"] = "Exercise name must be at least 3 characters long."

        if (
            self.suggested_min_reps is not None
            and self.suggested_max_reps is not None
            and self.suggested_min_reps > self.suggested_max_reps
        ):
            errors["suggested_max_reps"] = (
                "Maximum reps must be greater than or equal to minimum reps."
            )

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
