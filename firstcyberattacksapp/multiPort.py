from django.conf import settings


class MultiPortMiddleware(object):
    """
    Middleware changes the SESSION_COOKIE_NAME to use the current port in the name
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        settings.SESSION_COOKIE_NAME = 'sessionid' + request.META['SERVER_PORT']
        return None