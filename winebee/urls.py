# -*- encoding: UTF-8 -*-

'''
Copyright (c) 2012 - Adrián Rodríguez Vargas - www.adrianrodriguez.es

AUTHOR: Adrián Rodríguez Vargas <info@adrianrodriguez.es>

This file is part of Winebee.

Winebee is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Winebee is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Winebee.  If not, see <http://www.gnu.org/licenses/>.
'''

from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', 'frontend.views.home', name='home'),    
    url(r'^getdata/(?P<id>\d+)$', 'frontend.views.getdata', name='getdata'),
    url(r'^getdata/$', 'frontend.views.getdata', name='getdata'),
    url(r'^showdata/(?P<id>\d+)$', 'frontend.views.showdata', name='showdata'),
    
    # url(r'^$', 'winebee.views.home', name='home'),
    # url(r'^winebee/', include('winebee.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)
