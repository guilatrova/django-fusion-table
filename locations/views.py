from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from locations.models import Location
from locations.serializers import LocationSerializer
from fusiontables.permissions import ManageFusionTablePermission
from fusiontables.factories import GoogleAuthFactory

def index(request):
    request.session['google_auth_code'] = request.GET.get('code', None)
    return render(request, 'index.html')

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    authentication_classes = []
    permission_classes = [ManageFusionTablePermission, ]    

    def destroy_all(self, request):
        self.queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

    def perform_create(self, serializer):
        service = self._get_service()
        service.save_location(serializer.data)
        
        super(LocationViewSet, self).perform_create(serializer)

    def _get_service(self):
        googleAuth = GoogleAuthFactory()
        credentials = googleAuth.build_credentials(self.request.session['google_auth_code'])
        return googleAuth.build_service(credentials)