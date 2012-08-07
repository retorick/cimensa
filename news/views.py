# Create your views here.
from django.template import Context, RequestContext
from django.shortcuts import render_to_response

from news import News

def index(request):
    myNews = News()
    data = {
        'page_title': myNews.page_title,
        'articles': myNews.articles,
    }
    c = RequestContext(request, data)
    return render_to_response('news/index.html', c)

def article(request, news_id):
    myNews = News()
    data = {
        'page_title': myNews.page_title,
        'article': myNews.get_by_id(news_id),
    }
    c = RequestContext(request, data)
    return render_to_response('news/article.html', data)
