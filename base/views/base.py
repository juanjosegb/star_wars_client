from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView


class Index(LoginRequiredMixin, TemplateView):
    template_name = "base/index.html"
