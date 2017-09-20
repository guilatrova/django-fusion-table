from django.db import transaction
from django.shortcuts import render
from djgmaps.settings import GOOGLE_API_KEY
from rest_framework import viewsets, status
from rest_framework.response import Response
from locations.models import Location
from locations.serializers import LocationSerializer
from fusiontables.permissions import HasFusionTableCredentialsPermission, FusionTableNotExpiredPermission
from fusiontables.decorators import handle_code_received, redirect_if_not_authorized_to, uses_authorized_service

@handle_code_received
@redirect_if_not_authorized_to('/auth/')
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

    @transaction.atomic
    @uses_authorized_service
    def destroy_all(self, request, service):
        self.queryset.delete()
        service.clear_table()

        return Response(status=status.HTTP_204_NO_CONTENT)    

    @transaction.atomic
    @uses_authorized_service
    def perform_create(self, serializer, service):        
        super(LocationViewSet, self).perform_create(serializer)
        service.save_location(serializer.validated_data)