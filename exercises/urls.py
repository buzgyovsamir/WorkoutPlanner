from django.urls import include, path

from exercises.views import (
    ExerciseCreateView,
    ExerciseDeleteView,
    ExerciseDetailView,
    ExerciseListView,
    ExerciseUpdateView,
)

app_name = "exercises"

detail_patterns = [
    path("", ExerciseDetailView.as_view(), name="detail"),
    path("update/", ExerciseUpdateView.as_view(), name="update"),
    path("delete/", ExerciseDeleteView.as_view(), name="delete"),
]

urlpatterns = [
    path("", ExerciseListView.as_view(), name="list"),
    path("create/", ExerciseCreateView.as_view(), name="create"),
    path("<int:pk>/", include(detail_patterns)),
]
