from django.urls import path

from programs.views import (
    ProgramCreateView,
    ProgramDeleteView,
    ProgramDetailView,
    ProgramListView,
    ProgramUpdateView,
)

app_name = "programs"

urlpatterns = [
    path("", ProgramListView.as_view(), name="list"),
    path("create/", ProgramCreateView.as_view(), name="create"),
    path("<int:pk>/", ProgramDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", ProgramUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ProgramDeleteView.as_view(), name="delete"),
]
