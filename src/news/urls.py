from django.conf.urls import patterns, url
from news.views import edit,example,home

urlpatterns = patterns('news.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^new/$', 'example'),
)