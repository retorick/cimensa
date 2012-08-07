from django.db import models

# Create your models here.
class Article(models.Model):
    tagline = models.CharField(max_length = 255)
    article = models.TextField()
    post_date = models.DateField()
    exp_date = models.DateField()
    seq = models.IntegerField()

    def __unicode__(self):
        return self.tagline
