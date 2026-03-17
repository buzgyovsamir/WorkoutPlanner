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

    def get_queryset(self):
        queryset = Exercise.objects.prefetch_related("workouts")
        exercise_type = self.request.GET.get("type")
        sort = self.request.GET.get("sort", "name")

        

        if exercise_type:
            queryset = queryset.filter(exercise_type=exercise_type)

        if sort == "type":
            return queryset.order_by("exercise_type", "name")
        return queryset.order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_type"] = self.request.GET.get("type", "")
        context["current_sort"] = self.request.GET.get("sort", "name")
        return context


class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = "exercises/exercise_detail.html"
    context_object_name = "exercise"

    def get_queryset(self):
        return Exercise.objects.prefetch_related("workouts")


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
