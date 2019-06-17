from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class CustomExceptionHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if settings.DEBUG:
            with open('log.txt', 'w+') as log_file:
                log_file.write('custom error middleware logs error with args {} and  error class name {} : {}'.format(
                    exception.args, exception.__class__.__name__, '\n'))
        return None
