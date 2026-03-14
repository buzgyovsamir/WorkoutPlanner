from django.contrib import admin
from exercises.models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "exercise_type")
    search_fields = ("name",)
    list_filter = ("exercise_type",)
