from django.db import models


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

    def __str__(self):
        return f"{self.title} - {self.date}"
