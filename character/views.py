from django.shortcuts import render
from django.views.generic import TemplateView
from consumer.views import characters


class CharacterDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        character_information_list = characters.get_character(pk)
        character_names = character_information_list.keys()
        character_info = character_information_list.values()
        return render(request, "character.html", {'character_names': character_names, 'character_info': character_info})