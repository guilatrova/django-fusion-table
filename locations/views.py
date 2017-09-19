from django.shortcuts import render
from djgmaps.settings import CREDENTIALS_KEY, GOOGLE_API_KEY
from rest_framework import viewsets, status
from rest_framework.response import Response
from locations.models import Location
from locations.serializers import LocationSerializer
from fusiontables.permissions import HasFusionTableCredentialsPermission, FusionTableNotExpiredPermission
from fusiontables.factories import GoogleAuthFactory
from fusiontables.decorators import handle_code_received, redirect_if_not_authorized, uses_authorized_service

@handle_code_received
@redirect_if_not_authorized
def index(request):
    context = {
        'googleApiKey': GOOGLE_API_KEY
    }
    return render(request, 'index.html', context)

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    authentication_classes = []
    permission_classes = [HasFusionTableCredentialsPermission, FusionTableNotExpiredPermission]    

    @uses_authorized_service
    def destroy_all(self, request, service):
        service.clear_table()
        self.queryset.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)    

    @uses_authorized_service
    def perform_create(self, serializer, service):        
        service.save_location(serializer.validated_data)

        super(LocationViewSet, self).perform_create(serializer)