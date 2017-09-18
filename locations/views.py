from django.shortcuts import render
from rest_framework import viewsets
from locations.models import Location
from locations.serializers import LocationSerializer

def index(request):
    return render(request, 'index.html')

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()