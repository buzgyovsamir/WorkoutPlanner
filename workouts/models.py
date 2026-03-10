from django.db import models

from exercises.models import Exercise
from programs.models import Program


class Workout(models.Model):
    title = models.CharField(
        max_length=100,

    )
    date = models.DateField(
        auto_now=True,
    )
    duration_minutes = models.IntegerField()
    notes = models.TextField()
    program = models.ForeignKey(
        to=Program
    )
    exercises = models.ManyToManyField(
        to=Exercise
    )

    def __str__(self):
        return f"{self.title} - {self.date}"
