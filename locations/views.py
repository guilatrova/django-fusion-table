from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from locations.models import Location
from locations.serializers import LocationSerializer
from fusiontables.permissions import ManageFusionTablePermission
from fusiontables.factories import GoogleAuthFactory
from djgmaps.settings import CREDENTIALS_KEY

googleAuth = GoogleAuthFactory()

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

@redirect_if_not_authorized
@handle_code_received
def index(request):
    return render(request, 'index.html')

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    authentication_classes = []
    permission_classes = [ManageFusionTablePermission, ]    

    def destroy_all(self, request):
        service = self._get_service()
        service.clear_table()
        self.queryset.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)    

    def perform_create(self, serializer):
        service = self._get_service()
        service.save_location(serializer.validated_data)

        super(LocationViewSet, self).perform_create(serializer)

    def _get_service(self):
        credentials = self.request.session[CREDENTIALS_KEY]
        return googleAuth.build_service(credentials)