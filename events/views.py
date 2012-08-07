from django.template import Context, RequestContext
from django.shortcuts import render_to_response

from events import Events

def index(request):
    data = {
        'page_title': 'Calendar',
    }
    c = RequestContext(request, data)
    return render_to_response('calendar/index.html', c)
