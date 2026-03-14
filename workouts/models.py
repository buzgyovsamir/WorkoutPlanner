from django.db import models
from django.core.exceptions import ValidationError


class Workout(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    duration_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    program = models.ForeignKey(
        "programs.Program",
        on_delete=models.CASCADE,
        related_name="workouts",
    )
    exercises = models.ManyToManyField(
        to="exercises.Exercise",
        related_name="workouts",
        blank=True,
    )

    def clean(self):
        if self.title:
            self.title = self.title.strip()

        errors = {}

        if len(self.title) < 3:
            errors["title"] = "Workout name must be at least 3 characters long."

        if self.duration_minutes is not None and self.duration_minutes < 1:
            errors["duration_minutes"] = "Duration must be at least 1 minute."

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.date}"
