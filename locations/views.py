from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from locations.models import Location
from locations.serializers import LocationSerializer

def index(request):
    request.session['google_auth_code'] = request.GET.get('code', None)
    return render(request, 'index.html')

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    def destroy_all(self, request):
        self.queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)