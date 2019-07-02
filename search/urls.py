from django.urls import path
from search import views

urlpatterns = [
    path('search/', views.search_films, name='search'),
    path('search_list/', views.SearchView.as_view(), name='search_list')
]
