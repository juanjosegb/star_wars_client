from django.shortcuts import render
from django.views.generic import TemplateView
from consumer.views import films


class FilmDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        film_information_list = films.get_film(pk)
        film_names = film_information_list.keys()
        film_info = film_information_list.values()
        return render(request, "film.html", {'film_names': film_names, 'film_info': film_info})