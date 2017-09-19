from django.http import HttpResponseRedirect
from fusiontables.factories import GoogleAuthFactory

def auth(request):
    googleAuth = GoogleAuthFactory()
    url = googleAuth.build_authorization_url()
    return HttpResponseRedirect(url)