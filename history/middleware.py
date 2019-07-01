from history.utils import save_history_page


class SetLastVisitMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_response(self, request, response):
        if request.user.is_authenticated():
            save_history_page(request.user, request.path_info)

        return response
