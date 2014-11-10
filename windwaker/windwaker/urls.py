from django.conf.urls import patterns, include, url
from django.contrib import admin
from skyshaker import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^skyshaker/', include('skyshaker.urls')),
    url(r'^community-guidelines/$', views.community, name='community'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^donate/', views.donate, name='donate'),
    url(r'projects/(?P<slug>[^\./]+)$', views.project, name='project'),
    url(r'projects/(?P<slug>[^\./]+)/edit$', views.projectEdit, name='projectEdit'),
    url(r'^profiles/(?P<slug>[^\./]+)$', views.profile, name='profile'),
    url(r'^profiles/(?P<slug>[^\./]+)/edit$', views.profileEdit, name='profileEdit'),
    url(r'^search/', views.search, name='search'),
    url(r'^contribute/$', views.contribute, name='contribute'),
    url(r'^makerspaces/$', views.makerspaces, name='makerspaces'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^team/$', views.team, name='team'),
    url(r'^donate/$', views.donate, name='donate'),
    url(r'^login/$', views.user_login, name='login'),
#    url(r'^geodream/$', views.geodream, name='geodream'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
