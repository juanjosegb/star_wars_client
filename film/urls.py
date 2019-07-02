from django.urls import path
from film import views

urlpatterns = [
    path('film/<int:pk>', views.FilmDetailView.as_view(), name='film')
]