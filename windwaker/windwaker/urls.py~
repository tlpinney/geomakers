from django.conf.urls import patterns, include, url
from django.contrib import admin
from skyshaker import views

urlpatterns = patterns('',
    url(r'^skyshaker/', include('skyshaker.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^donate/', views.donate, name='donate'),
    url(r'projects/(?P<slug>[^\.]+)', views.project, name='project'),
)
