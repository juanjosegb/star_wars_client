from django.urls import path
from search import views

urlpatterns = [
    path('search/', views.search_films, name='search'),
    path('film/<int:pk>', views.FilmDetailView.as_view(), name='film')
]
