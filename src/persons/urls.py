from django.conf.urls import patterns, url


urlpatterns = patterns('persons.views',
                       url(r'^$', 'user_home', name='user-home'),
)