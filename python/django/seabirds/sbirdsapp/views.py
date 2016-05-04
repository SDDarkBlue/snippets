from django.core import serializers
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from sbirdsapp.models import Observation
from restless.views import Endpoint
from sbirdsapp.forms import ObservationForm

# Create your views here.
def get_observations_as_json():
    data = Observation.objects.all()
    observations = []
    for data_point in data:
        print data_point
        observation = {
            'pk': str(data_point.pk),
            'time': str(data_point.time),
            'species': str(data_point.species.name),
            'count': str(data_point.count),
            'age': str(data_point.age.code),
            'plumage': str(data_point.plumage.code),
            'stratum': str(data_point.stratum.code),
            'behaviour flyway': str(data_point.behaviour_fly.code),
            'association behaviour': str(data_point.ass_behaviour.code)
        }
        observations.append(observation)
    return observations

def list_observations(request):
    return render_to_response('observations.html', {'observations': get_observations_as_json})

class GetObservations(Endpoint):
    def get(self, request):
        return get_observations_as_json()

def add_observation(request):
    if request.method == 'POST':
        form = ObservationForm(request.POST)
        print('form posted with POST data: {0}'.format(str(request.POST)))
        if form.is_valid():
            trip = form.cleaned_data['trip']
            time = form.cleaned_data['time']
            species = form.cleaned_data['species']
            count = form.cleaned_data['count']
            age = form.cleaned_data['age']
            plumage = form.cleaned_data['plumage']
            stratum = form.cleaned_data['stratum']
            behaviour_flyway = form.cleaned_data['behaviour_fly']
            association_behaviour = form.cleaned_data['ass_behaviour']
            print('POST data received: {0}'.format(str(request.POST)))

            o = Observation(trip=trip, time=time, species=species, count=count, age=age, plumage=plumage, stratum=stratum, behaviour_fly=behaviour_flyway, ass_behaviour=association_behaviour)
            o.save()
            return HttpResponseRedirect('/')
    else:
        form = ObservationForm()

    return render(request, 'new_observation.html', {'form': form})
