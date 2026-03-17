from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from programs.models import Program
from workouts.forms import WorkoutAssignExercisesForm, WorkoutForm
from workouts.models import Workout


class WorkoutListView(ListView):
    model = Workout
    template_name = "workouts/workout_list.html"
    context_object_name = "workouts"

    def get_queryset(self):
        queryset = Workout.objects.select_related("program").prefetch_related("exercises")
        program_id = self.request.GET.get("program")
        sort = self.request.GET.get("sort", "date_desc")
        

        if program_id:
            queryset = queryset.filter(program_id=program_id)



        if sort == "title":
            queryset = queryset.order_by("title")
        elif sort == "date_asc":
            queryset = queryset.order_by("date")
        else:
            queryset = queryset.order_by("-date", "title")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["programs"] = Program.objects.order_by("name")
        context["current_program"] = self.request.GET.get("program", "")
        context["current_sort"] = self.request.GET.get("sort", "date_desc")
        return context


class WorkoutDetailView(DetailView):
    model = Workout
    template_name = "workouts/workout_detail.html"
    context_object_name = "workout"

    def get_queryset(self):
        return Workout.objects.select_related("program").prefetch_related("exercises")


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
    template_name = "exercises/exercise_assign_form.html"
    success_message = "Exercises assigned successfully."

    def get_success_url(self):
        return reverse_lazy("workouts:detail", kwargs={"pk": self.object.pk})
