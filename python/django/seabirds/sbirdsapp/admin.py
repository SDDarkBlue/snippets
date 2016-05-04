from django.contrib import admin
from sbirdsapp.models import Age, Association_Behaviour_B, Behaviour_Flyway_C, Count_Method, Observer, Octant, Plumage, Ship, Species_Count_Method, Stratum, Turbine_Height, Visibility, Wave_Height, Wind_Speed, Taxon, Observation, Trip

# Register your models here.
#from django.db import models

admin.site.register(Age)
admin.site.register(Association_Behaviour_B)
admin.site.register(Behaviour_Flyway_C)
admin.site.register(Count_Method)
admin.site.register(Observer)
admin.site.register(Octant)
admin.site.register(Plumage)
admin.site.register(Ship)
admin.site.register(Species_Count_Method)
admin.site.register(Stratum)
admin.site.register(Turbine_Height)
admin.site.register(Visibility)
admin.site.register(Wave_Height)
admin.site.register(Wind_Speed)
admin.site.register(Taxon)
admin.site.register(Observation)
admin.site.register(Trip)
