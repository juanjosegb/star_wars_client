from django.urls import path
from base import views

urlpatterns = [
    path('index/', views.Index.as_view(), name='index')
]
