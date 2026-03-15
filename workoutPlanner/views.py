from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "core/home.html"


def custom_404(request, exception):
    return render(request, "404.html", status=404)
