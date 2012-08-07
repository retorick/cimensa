from articles.models import Category

def subnav():
    categories = Category.objects.all()
    return categories
