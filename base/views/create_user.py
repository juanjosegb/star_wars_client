from django.urls import reverse_lazy
from django.views.generic import CreateView

from base.forms import CustomUserCreationForm

class CustomUserAdmin(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/create_user.html'
    success_url = reverse_lazy('index')
