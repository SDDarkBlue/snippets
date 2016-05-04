from django.conf.urls import patterns, include, url
from sbirdsapp.views import list_observations, GetObservations, add_observation

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'seabirds.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     (r"^grid$", list_observations),
     (r"^get$", GetObservations.as_view()),
     (r"^add_own$", add_observation),
)
