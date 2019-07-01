from django.urls import path
from history import views

urlpatterns = [
    path('history_list/<int:pk>', views.HistoryListView.as_view(), name='history_list')
]
