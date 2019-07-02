from braces.views import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from consumer.views import films


class FilmDetailView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        film_information_list = films.get_film(pk)
        return render(request, "film.html", {'film_info': film_information_list})