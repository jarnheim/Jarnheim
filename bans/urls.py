from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('bans.views',
    url(r'^$', 'index'),
    url(r'^(?P<ban_id>\d+)/$', 'detail'),                   
)
