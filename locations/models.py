from django.db import models

class Location(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=120)

    class Meta:
        unique_together = ('lat', 'lon',)

    def __repr__(self):
        return '(lat: {} lon: {})'.format(self.lat, self.lon)