# Create your views here.
from django.template import Context, RequestContext
from django.shortcuts import render_to_response

from home import Home
from words.words import Words
from nav import subnav

def index(request):
    myHome = Home()
    myGame = Words()
    words = myGame.words
    correct = myGame.correct 
    data = {
        'page_title': myHome.page_title,
        'words': words,
        'correct': correct,
        'correctword': words[correct].word,
        'correctdef': words[correct].definition,
    }
    c = RequestContext(request, data)
    return render_to_response('index.html', c)

def about(request):
    myHome = Home()
    myHome.about()

    categories = subnav()
    data = {
        'page_title' : myHome.page_title,
        'article_categories' : categories,
    }

    c = RequestContext(request, data)
    return render_to_response('about.html', c)
