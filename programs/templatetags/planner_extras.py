from django import template

from exercises.models import Exercise
from programs.models import Program
from workouts.models import Workout

register = template.Library()


@register.filter
def format_exercise_type(value):
    return str(value).replace("_", " ").title()


@register.filter
def exercise_badge_class(value):
    if value == "compound":
        return "bg-primary-subtle text-primary-emphasis"
    if value == "hypertrophy":
        return "bg-success-subtle text-success-emphasis"
    return "bg-secondary-subtle text-secondary-emphasis"


@register.inclusion_tag("common/summary_cards.html")
def planner_summary():
    return {
        "program_count": Program.objects.count(),
        "workout_count": Workout.objects.count(),
        "exercise_count": Exercise.objects.count(),
    }
