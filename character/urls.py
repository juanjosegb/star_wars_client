from django.urls import path
from character import views

urlpatterns = [
    path('film/<int:pk>', views.CharacterDetailView.as_view(), name='film')
]