from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.views.generic.simple import direct_to_template

# Enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jarnheim.views.home', name='home'),
    # url(r'^jarnheim/', include('jarnheim.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^/$', 'views.index'),
    url(r'^$', direct_to_template, {'template': 'index.html'}),

    # Enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^bans/', include('bans.urls', namespace="bans")),
    )
