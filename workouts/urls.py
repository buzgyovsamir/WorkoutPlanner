from django.urls import path

from workouts.views import (
    WorkoutAssignExercisesView,
    WorkoutCreateView,
    WorkoutDeleteView,
    WorkoutDetailView,
    WorkoutListView,
    WorkoutUpdateView,
)

app_name = "workouts"

urlpatterns = [
    path("", WorkoutListView.as_view(), name="list"),
    path("create/", WorkoutCreateView.as_view(), name="create"),
    path("<int:pk>/", WorkoutDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", WorkoutUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", WorkoutDeleteView.as_view(), name="delete"),
    path(
        "<int:pk>/assign-exercises/",
        WorkoutAssignExercisesView.as_view(),
        name="assign-exercises",
    ),
]
