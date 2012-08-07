from django.forms import *
from django.db.models import *
from django.contrib import admin
from public_html.articles.models import Category, Member_article
from tinymce.widgets import TinyMCE

class Member_articleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))

    class Meta:
        model = Member_article

class Member_articleAdmin(admin.ModelAdmin):
    form = Member_articleForm()

admin.site.register(Category)
admin.site.register(Member_article)
