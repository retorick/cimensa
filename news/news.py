from models import Article

class News:
    def __init__(self):
        self.page_title = "News"
        self.articles = Article.objects.all()        

    def get_by_id(self, news_id):
        article = Article.objects.get(pk=news_id)
        return article
