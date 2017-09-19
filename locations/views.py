from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from locations.models import Location
from locations.serializers import LocationSerializer
from fusiontables.permissions import ManageFusionTablePermission
from fusiontables.factories import GoogleAuthFactory
from djgmaps.settings import CREDENTIALS_KEY
from locations.decorators import handle_code_received, redirect_if_not_authorized, get_authorized_service

googleAuth = GoogleAuthFactory()

@redirect_if_not_authorized
@handle_code_received
def index(request):
    return render(request, 'index.html')

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    authentication_classes = []
    permission_classes = [ManageFusionTablePermission, ]    

    @get_authorized_service
    def destroy_all(self, request, service):
        service.clear_table()
        self.queryset.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)    

    @get_authorized_service
    def perform_create(self, serializer, service):        
        service.save_location(serializer.validated_data)

        super(LocationViewSet, self).perform_create(serializer)