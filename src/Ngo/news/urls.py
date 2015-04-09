from django.conf.urls import patterns, url

urlpatterns = patterns('Ngo.news.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^new/$', 'create_article'),
)