from django.shortcuts import render_to_response
from bans.models import Ban

def index(request):
    all_bans = Ban.objects.all().order_by('-end_dtm', '-start_dtm')
    return render_to_response('index.html', {'bans': all_bans})

def detail(request, ban_id):
    ban = Ban.objects.get(pk=ban_id)
    return render_to_response('detail.html', {'ban': ban})
