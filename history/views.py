from django.views.generic import ListView
from history.models import History


class HistoryListView(ListView):
    model = History
    template_name = "history_list.html"
