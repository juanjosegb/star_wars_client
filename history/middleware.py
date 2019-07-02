from history.utils import save_history_page


class SetLastVisitMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response

    def process_request(self, request):
        if request.user.is_authenticated:
            save_history_page(request.path_info, request.user)
        return None