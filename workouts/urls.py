from django.urls import include, path

from workouts.views import (
    WorkoutAssignExercisesView,
    WorkoutCreateView,
    WorkoutDeleteView,
    WorkoutDetailView,
    WorkoutListView,
    WorkoutUpdateView,
)

app_name = "workouts"

detail_patterns = [
    path("", WorkoutDetailView.as_view(), name="detail"),
    path("update/", WorkoutUpdateView.as_view(), name="update"),
    path("delete/", WorkoutDeleteView.as_view(), name="delete"),
    path(
        "assign-exercises/",
        WorkoutAssignExercisesView.as_view(),
        name="assign-exercises",
    ),
]

urlpatterns = [
    path("", WorkoutListView.as_view(), name="list"),
    path("create/", WorkoutCreateView.as_view(), name="create"),
    path("<int:pk>/", include(detail_patterns)),
]
