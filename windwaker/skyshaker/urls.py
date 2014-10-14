from django.conf.urls import patterns, url
from skyshaker import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'projects/(?P<slug>[^\.]+)', views.project, name='project'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profiles/$', views.profile, name='profile'),
    url(r'^search/$', views.search, name='search'),
    url(r'^geodream/$', views.geodream, name='geodream'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
