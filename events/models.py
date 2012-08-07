from django.db import models

class Calendar_category(models.Model):
    category = models.CharField(max_length=255)
    seq = models.IntegerField()

    def __unicode__(self):
        return self.category

class Calendar(models.Model):
    date = models.DateField()
    seq = models.IntegerField()
    item = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Calendar_category)

    def __unicode__(self):
        return self.item
