# -*- coding: utf-8 -*-  
from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$', "mysite.views.index"),
    (r'^logout/','mysite.views.sfile'),
    (r'^sfile/','mysite.views.sfile'),
    (r'^tfile/','mysite.views.tfile'),
    (r'^update/','mysite.views.update'),
    (r'^news/','mysite.views.news'),
    (r'^logout/$', 'mysite.views.logout'),  
    (r'^uploadfile/', include('uploadfile.urls')),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    url(r'^admin/', include(admin.site.urls)),
    )