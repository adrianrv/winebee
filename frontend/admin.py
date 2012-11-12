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

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from models import Node, Data
from django.utils.translation import ugettext_lazy as _

admin.site.register (Node)

class DataAdmin (admin.ModelAdmin):
    def custom_date(self, obj):
        return obj.date.strftime('%d %b %Y %H:%M:%S')
    def node__id(self, obj):
        return obj.node.id
    custom_date.short_description = _(u'Date')
    list_display = ('id', 'node__id', 'node', 'custom_date', 'temperature', 'humidity', 'luminosity')

admin.site.register (Data, DataAdmin)
admin.site.unregister (Site)
