from django import forms
from sbirdsapp.models import Age, Association_Behaviour_B, Behaviour_Flyway_C, Count_Method, Observer, Octant, Plumage, Ship, Species_Count_Method, Stratum, Turbine_Height, Visibility, Wave_Height, Wind_Speed, Taxon, Observation, Trip

class ObservationForm(forms.Form):
    trip = forms.ModelChoiceField(queryset=Trip.objects.all())
    time = forms.TimeField()
    species = forms.ModelChoiceField(queryset=Taxon.objects.all())
    count = forms.IntegerField()
    age = forms.ModelChoiceField(queryset=Age.objects.all())
    plumage = forms.ModelChoiceField(queryset=Plumage.objects.all())
    stratum = forms.ModelChoiceField(queryset=Stratum.objects.all())
    ass_behaviour = forms.ModelChoiceField(queryset=Association_Behaviour_B.objects.all())
    behaviour_fly = forms.ModelChoiceField(queryset=Behaviour_Flyway_C.objects.all())
