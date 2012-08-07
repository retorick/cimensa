from models import Member_article

class Articles:
    def __init__(self):
       self.articles = Member_article.objects.all()

    def get_by_id(self, article_id):
        article = Member_article.objects.get(pk=article_id)
        return article
