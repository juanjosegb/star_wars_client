
def search(films, search_for):
    films_matches = dict()
    for key in films.keys():
        if search_for in key:
            films_matches[key] = films[key][0].rsplit('/', 1)[1]
    return films_matches
