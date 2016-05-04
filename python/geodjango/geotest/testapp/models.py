from django.contrib.gis.db import models

"""
# Create your models here.
class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    def __str__(self):
        return self.name
"""

class Bird(models.Model):
    species = models.CharField(max_length=50)
    ring_code = models.CharField(max_length=20)
    color_ring_code = models.CharField(max_length=20)
    sex = models.CharField(max_length=20, choices= (('female', 'female'), ('male', 'male')))
    weight_in_g = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tracking_start_date_time = models.DateTimeField()
    tracking_end_date_time = models.DateTimeField(blank=True, null=True)
    colony_latitude = models.FloatField()
    colony_longitude = models.FloatField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    bird_name = models.TextField(blank=True, null=True)
    colony_name = models.CharField(max_length=20)
    colony_location = models.PointField(blank=True, null=True, geography=True)

    def __str__(self):
        return '{0}, {1}'.format(self.species, self.id)

class Log(models.Model):
    bird = models.ForeignKey(Bird)
    timestamp = models.DateTimeField()
    lon = models.FloatField()
    lat = models.FloatField()
    point = models.PointField(blank=True, null=True, geography=True)

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    objects = models.GeoManager()

    def getDistanceTravelled(self):
        previous_logs = self.bird.log_set.filter(timestamp__lt=self.timestamp).order_by('-timestamp')
        previous_log = previous_logs[0]
        d = previous_log.point.distance(self.distance)
        # or: previous_logs.distance(self.distance)[0] ; returns Distance object
        return d

    def __str__(self):
        return '{0}: {1}'.format(self.bird, self.timestamp)

class WorldBorder(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return self.name

