from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^', include('news.urls')),
                       url(r'^user/', include('persons.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'login.html'},
                           name='login'),
)
