# Create your views here.
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse

from words import Words

def index(request):
    myWords = Words()
    data = {
        'words': myWords.words, 
        'correct': myWords.correct
    }
    c = RequestContext(request, data)
    return render_to_response('words/index.html', c)

