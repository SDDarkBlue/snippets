from django.db import models

# Create your models here.
class ControlledVocabulary(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=20)
    deprecated = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0} | {1}'.format(self.code, self.name)

class Age(ControlledVocabulary):
    pass
class Association_Behaviour_B(ControlledVocabulary):
    pass
class Behaviour_Flyway_C(ControlledVocabulary):
    pass
class Count_Method(ControlledVocabulary):
    pass
class Observer(ControlledVocabulary):
    pass
class Octant(ControlledVocabulary):
    pass
class Plumage(ControlledVocabulary):
    pass
class Ship(ControlledVocabulary):
    pass
class Species_Count_Method(ControlledVocabulary):
    pass
class Stratum(ControlledVocabulary):
    pass
class Turbine_Height(ControlledVocabulary):
    pass
class Visibility(ControlledVocabulary):
    pass
class Wave_Height(ControlledVocabulary):
    pass
class Wind_Speed(ControlledVocabulary):
    pass

class Taxon(models.Model):
    INBOcode = models.CharField(max_length=10)
    name = models.CharField(max_length=60)
    def __unicode__(self):
        return u'{0} | {1}'.format(self.INBOcode, self.name)

class Trip(models.Model):
    survey = models.CharField(max_length=10)
    date = models.DateField()
    observer = models.ForeignKey(Observer)
    tripid = models.CharField(max_length=10)
    ship = models.ForeignKey(Ship)

class Observation(models.Model):
    trip = models.ForeignKey(Trip)
    time = models.TimeField()
    species = models.ForeignKey(Taxon)
    count = models.IntegerField()
    age = models.ForeignKey(Age)
    plumage = models.ForeignKey(Plumage)
    stratum = models.ForeignKey(Stratum)
    ass_behaviour = models.ForeignKey(Association_Behaviour_B)
    behaviour_fly = models.ForeignKey(Behaviour_Flyway_C)

    def __unicode__(self):
        return u'{0} {1} {2}'.format(self.time, self.species, self.count)
