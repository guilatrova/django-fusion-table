from django.http import HttpResponseRedirect
from djgmaps.settings import CREDENTIALS_KEY
from fusiontables.factories import GoogleAuthFactory

def redirect_if_not_authorized(func):
    '''
    Checks if user has valid credentials to access FusionTable API.
    If not, redirects to '/auth' endpoint.
    Expects to receive a request object in *args.
    '''
    def _wrapper(request):
        if CREDENTIALS_KEY not in request.session:
            return HttpResponseRedirect('/auth/')
        return func(request)

    return _wrapper

def handle_code_received(func):
    '''
    Handles code received from Google API callback.
    If it's received then save credentials in session.
    Expects to receive a request object in *args.
    '''
    def _wrapper(request):
        code = request.GET.get('code', False)
        if code:
            googleAuth = GoogleAuthFactory()
            request.session[CREDENTIALS_KEY] = googleAuth.build_credentials(code)

        return func(request)
        
    return _wrapper

def uses_authorized_service(func):
    '''
    Injects authorized FusionTableService in function.
    Expects to receive an instance with access to request.
    '''
    def _wrapper(self, *args, **kwargs):
        googleAuth = GoogleAuthFactory()
        credentials = self.request.session[CREDENTIALS_KEY]
        kwargs['service'] = googleAuth.build_service(credentials)

        return func(self, *args, **kwargs)

    return _wrapper