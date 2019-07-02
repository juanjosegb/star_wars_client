from django.urls import path
from starship import views

urlpatterns = [
    path('starship/<int:pk>', views.StarshipDetailView.as_view(), name='starship')
]