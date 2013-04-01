from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('accounts.views',
    url(r'^login/$', 'login'),
    url(r'^profile/$', 'profile'),
    url(r'^org/(?P<uid>[A-Za-z0-9-_]+)/$', 'org')
)