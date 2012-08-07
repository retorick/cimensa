from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from public_html import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'public_html.views.home', name='home'),
    # url(r'^public_html/', include('public_html.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index'),
    url(r'^words$', 'words.views.index'),
    url(r'^about$', 'home.views.about'),
    url(r'^news$', 'news.views.index'),
    url(r'^news/(?P<news_id>\d+)/', 'news.views.article'),
    url(r'^articles', include('public_html.articles.urls')),
    url(r'^calendar$', 'public_html.events'),
    url(r'^playground/?$', 'playground.views.index'),
    url(r'^playground/addition$', 'playground.views.addition'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    url(r'^tinymce/', include('tinymce.urls')),
)
