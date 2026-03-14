from django.contrib import admin
from workouts.models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "program")
    search_fields = ("title",)
    list_filter = ("program",)
