from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.views.generic import list_detail
from bans.models import Ban

banlist_info = {'queryset': Ban.objects.all().order_by('-end_dtm',
                                                       '-start_dtm'),
                'template_name': 'ban_list.html',
                'template_object_name': "ban"}
ban_info = {'queryset': Ban.objects.all(),
            'template_name': 'ban_detail.html',
            'template_object_name': "ban"}

urlpatterns = patterns('bans.views',
    url(r'^$', list_detail.object_list, banlist_info),
    url(r'^(?P<object_id>\d+)/$', list_detail.object_detail, ban_info),                   
)
