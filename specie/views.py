from django.shortcuts import render
from django.views.generic import TemplateView
from consumer.views import species


class SpecieDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        specie_information_list = species.get_specie(pk)
        specie_names = specie_information_list.keys()
        specie_info = specie_information_list.values()
        return render(request, "specie.html", {'specie_names': specie_names, 'planet_info': specie_info})