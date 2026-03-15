from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from exercises.forms import ExerciseForm
from exercises.models import Exercise


class ExerciseListView(ListView):
    model = Exercise
    template_name = "exercises/exercise_list.html"
    context_object_name = "exercises"


class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = "exercises/exercise_detail.html"
    context_object_name = "exercise"


class ExerciseCreateView(SuccessMessageMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = "exercises/exercise_form.html"
    success_url = reverse_lazy("exercises:list")
    success_message = "Exercise created successfully."


class ExerciseUpdateView(SuccessMessageMixin, UpdateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = "exercises/exercise_form.html"
    success_url = reverse_lazy("exercises:list")
    success_message = "Exercise updated successfully."


class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = "exercises/exercise_confirm_delete.html"
    success_url = reverse_lazy("exercises:list")
    context_object_name = "exercise"

    def form_valid(self, form):
        messages.success(self.request, "Exercise deleted successfully.")
        return super().form_valid(form)
