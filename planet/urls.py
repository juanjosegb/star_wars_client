from django.urls import path
from planet import views

urlpatterns = [
    path('film/<int:pk>', views.PlanetDetailView.as_view(), name='planet')
]