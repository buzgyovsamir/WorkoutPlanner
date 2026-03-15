from django.urls import path

from exercises.views import (
    ExerciseCreateView,
    ExerciseDeleteView,
    ExerciseDetailView,
    ExerciseListView,
    ExerciseUpdateView,
)

app_name = "exercises"

urlpatterns = [
    path("", ExerciseListView.as_view(), name="list"),
    path("create/", ExerciseCreateView.as_view(), name="create"),
    path("<int:pk>/", ExerciseDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", ExerciseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ExerciseDeleteView.as_view(), name="delete"),
]
