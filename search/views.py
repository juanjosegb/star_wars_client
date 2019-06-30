from django.shortcuts import render
from search import utils

from consumer.views import all_films


def search_films(request):
    search_for = request.POST.get('search')
    films_list = all_films.get_all_film_names()
    result_list = utils.search(films_list, search_for)
    return render(request, 'results.html', result_list)
