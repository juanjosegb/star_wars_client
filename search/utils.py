
def search(films, search_for):
    films_matches = dict()
    for key in films.keys():
        if search_for in key:
            films_matches[key] = films[key]
    return films_matches
