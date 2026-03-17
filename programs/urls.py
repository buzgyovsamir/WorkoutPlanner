from django.urls import include, path

from programs.views import (
    ProgramCreateView,
    ProgramDeleteView,
    ProgramDetailView,
    ProgramListView,
    ProgramUpdateView,
)

app_name = "programs"

detail_patterns = [
    path("", ProgramDetailView.as_view(), name="detail"),
    path("update/", ProgramUpdateView.as_view(), name="update"),
    path("delete/", ProgramDeleteView.as_view(), name="delete"),
]

urlpatterns = [
    path("", ProgramListView.as_view(), name="list"),
    path("create/", ProgramCreateView.as_view(), name="create"),
    path("<int:pk>/", include(detail_patterns)),
]
