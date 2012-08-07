# Create your views here.
from django.template import Context, RequestContext
from django.shortcuts import render_to_response

from articles import Articles

def index(request):
    myArticles = Articles()
    data = {
        'page_title': 'Member Articles',
        'articles': myArticles.articles,
    }
    c = RequestContext(request, data)
    return render_to_response('articles/index.html', c)

def article(request, article_id):
    myArticles = Articles()
    data = {
        'page_title': 'Member Articles',
        'article': myArticles.get_by_id(article_id),
    }
    c = RequestContext(request, data)
    return render_to_response('articles/article.html', c)
