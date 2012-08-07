from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)
    seq = models.IntegerField()

    def __unicode__(self):
        return self.category

class Member_article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category)
    post_date = models.DateField()
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)

    class Admin:
        js = (
            '/tiny_mce/tiny_mce.js',
            '/static/js/admin/textarea.js',
        )

    def __unicode__(self):
        return self.title

