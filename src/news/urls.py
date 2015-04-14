from django.conf.urls import patterns, url
from src.news.views import edit,example

urlpatterns = patterns('news.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^new/$', 'example'),
)