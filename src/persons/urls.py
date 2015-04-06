from django.conf.urls import patterns, url
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('persons.views',
                       url(r'^$', 'user_home', name='user-home'),
)