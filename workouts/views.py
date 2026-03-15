from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from workouts.forms import WorkoutAssignExercisesForm, WorkoutForm
from workouts.models import Workout


class WorkoutListView(ListView):
    model = Workout
    template_name = "workouts/workout_list.html"
    context_object_name = "workouts"


class WorkoutDetailView(DetailView):
    model = Workout
    template_name = "workouts/workout_detail.html"
    context_object_name = "workout"


class WorkoutCreateView(SuccessMessageMixin, CreateView):
    model = Workout
    form_class = WorkoutForm
    template_name = "workouts/workout_form.html"
    success_url = reverse_lazy("workouts:list")
    success_message = "Workout created successfully."


class WorkoutUpdateView(SuccessMessageMixin, UpdateView):
    model = Workout
    form_class = WorkoutForm
    template_name = "workouts/workout_form.html"
    success_url = reverse_lazy("workouts:list")
    success_message = "Workout updated successfully."


class WorkoutDeleteView(DeleteView):
    model = Workout
    template_name = "workouts/workout_confirm_delete.html"
    success_url = reverse_lazy("workouts:list")
    context_object_name = "workout"

    def form_valid(self, form):
        messages.success(self.request, "Workout deleted successfully.")
        return super().form_valid(form)


class WorkoutAssignExercisesView(SuccessMessageMixin, UpdateView):
    model = Workout
    form_class = WorkoutAssignExercisesForm
    template_name = "workouts/workout_assign_exercises.html"
    success_message = "Exercises assigned successfully."

    def get_success_url(self):
        return reverse_lazy("workouts:detail", kwargs={"pk": self.object.pk})
