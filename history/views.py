from braces.views import LoginRequiredMixin
from django.views.generic import ListView
from history.models import History


class HistoryListView(LoginRequiredMixin, ListView):
    model = History
    template_name = "history_list.html"

    def get_context_data(self, **kwargs):
        context = super(HistoryListView, self).get_context_data(**kwargs)
        context['objects'] = History.objects.filter(user=self.request.user)
        return context
