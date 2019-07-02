from django.shortcuts import render
from django.views.generic import TemplateView
from consumer.views import planets


class PlanetDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        planet_information_list = planets.get_planet(pk)
        planet_names = planet_information_list.keys()
        planet_info = planet_information_list.values()
        return render(request, "planet.html", {'planet_names': planet_names, 'planet_info': planet_info})