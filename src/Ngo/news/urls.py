from django.conf.urls import patterns, url

urlpatterns = patterns('Ngo.news.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^new/$', 'create_article'),
                       url(r'^edit/$', 'edit'),
                       url(r'^article/(\d{1,7})/$', 'show_article'),
                       url(r'^article/(\d{1,7})/(\w{1,2})/$', 'update_news'),
                       url(r'^delete/(\d{1,7})/d/$', 'delete_news'),
                       url(r'^shownews/$', 'show_new_news'),
                       url(r'editnews/$', 'show_news'),
                       url(r'^accounts/profile/$', 'user_home'),
                       url(r'^news/(\w{1,2})/$', 'filter_news'),
)