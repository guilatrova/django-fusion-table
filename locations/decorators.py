from django.http import HttpResponseRedirect
from fusiontables.factories import GoogleAuthFactory
from djgmaps.settings import CREDENTIALS_KEY

def redirect_if_not_authorized(func):
    def _wrapper(request):
        if CREDENTIALS_KEY not in request.session:
            return HttpResponseRedirect('/auth/')
        return func(request)

    return _wrapper

def handle_code_received(func):
    def _wrapper(request):
        googleAuth = GoogleAuthFactory()
        code = request.GET.get('code', False)
        if code:
            request.session[CREDENTIALS_KEY] = googleAuth.build_credentials(code)

        return func(request)
        
    return _wrapper

def get_authorized_service(func):    
    def _wrapper(self, *args, **kwargs):
        googleAuth = GoogleAuthFactory()
        credentials = self.request.session[CREDENTIALS_KEY]
        kwargs['service'] = googleAuth.build_service(credentials)

        return func(self, *args, **kwargs)

    return _wrapper