from django.http import JsonResponse
from django.views.generic import TemplateView

from search import utils

from consumer.views import all_films


def search_films(request):
    search_for = request.POST.get('search')
    films_list = all_films.get_all_film_names()
    result_list = utils.search(films_list, search_for)
    return JsonResponse(result_list)


class SearchView(TemplateView):
    template_name = "search.html"

