# Create your views here.
from django.template import Context, RequestContext
from django.shortcuts import render_to_response


def index(request):
    data = {
        'page_title': 'Playground',
    }
    c = RequestContext(request, data)
    return render_to_response('playground/index.html', c)

def addition(request):
    data = {
        'page_title': 'Playground - Addition',
    }

    c = RequestContext(request, data)
    return render_to_response('playground/addition.html', c)
