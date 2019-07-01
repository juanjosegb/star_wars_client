from history.models import History


def save_history_page(url, user):
    history = History(user=user, page=url)
    history.save()
