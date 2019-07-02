from django.urls import path
from specie import views

urlpatterns = [
    path('specie/<int:pk>', views.SpecieDetailView.as_view(), name='specie')
]