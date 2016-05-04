from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'seabirds.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/sbirdsapp/observation/', include('sbirdsapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
