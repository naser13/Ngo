from django.conf.urls import patterns, url
from src.news.views import edit

urlpatterns = patterns('news.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^new/$', 'edit')
)