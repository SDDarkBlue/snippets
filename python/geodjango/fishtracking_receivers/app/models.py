from django.contrib.gis.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField(blank=True, null=True, geography=True, srid=4326)

    # overriding the default manager with a GeoManager instance.
    objects = models.GeoManager()

    def __str__(self):
        return self.name

class River(models.Model):
    name = models.CharField(max_length=200)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    def __str__(self):
        return self.name

class LineRiver(models.Model):
    name = models.CharField(max_length=200)
    geom = models.LineStringField(srid=4326)
    objects = models.GeoManager()
    def __str__(self):
        return self.name

class MultiLineRiver(models.Model):
    name = models.CharField(max_length=200)
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()
    def __str__(self):
        return self.name
