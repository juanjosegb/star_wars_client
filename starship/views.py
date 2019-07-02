from django.shortcuts import render
from django.views.generic import TemplateView
from consumer.views import starships


class StarshipDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        starship_information_list = starships.get_starship(pk)
        starship_names = starship_information_list.keys()
        starship_info = starship_information_list.values()
        return render(request, "starship.html", {'starship_names': starship_names, 'starship_info': starship_info})