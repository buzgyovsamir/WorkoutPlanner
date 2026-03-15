from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from programs.forms import ProgramForm
from programs.models import Program


class ProgramListView(ListView):
    model = Program
    template_name = "programs/program_list.html"
    context_object_name = "programs"


class ProgramDetailView(DetailView):
    model = Program
    template_name = "programs/program_detail.html"
    context_object_name = "program"


class ProgramCreateView(SuccessMessageMixin, CreateView):
    model = Program
    form_class = ProgramForm
    template_name = "programs/program_form.html"
    success_url = reverse_lazy("programs:list")
    success_message = "Program created successfully."


class ProgramUpdateView(SuccessMessageMixin, UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = "programs/program_form.html"
    success_url = reverse_lazy("programs:list")
    success_message = "Program updated successfully."


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "programs/program_confirm_delete.html"
    success_url = reverse_lazy("programs:list")
    context_object_name = "program"

    def form_valid(self, form):
        messages.success(self.request, "Program deleted successfully.")
        return super().form_valid(form)
