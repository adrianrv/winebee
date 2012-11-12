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

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from datetime import datetime

class Node (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(_(u'Name'),max_length=100,null=False, blank=False)
    description = models.CharField(_(u'Description'), max_length=600, null=True, blank=True)
    def __unicode__(self):
        return u'%s' % (self.name)
    class Meta:
        db_table = settings.DB_PREFIX + 'node'
        verbose_name = _(u'Node')
        verbose_name_plural = _(u'Nodes')

class Data (models.Model):
    id = models.AutoField(primary_key=True)
    node = models.ForeignKey(Node, verbose_name=_(u'Node'), null=False, blank=False)
    # gateway.py script makes the convertion to degres
    temperature = models.DecimalField(_(u'Temperature'), max_digits=4, decimal_places=2, null=False, blank=False)
    humidity = models.IntegerField(_(u'Humidity'),max_length=4,null=False, blank=False)
    luminosity = models.IntegerField(_(u'Luminosity'),max_length=4,null=False, blank=False)
    date = models.DateTimeField(_(u'Date'), default=datetime.now, null=False, blank=False)
    def __unicode__(self):
        return u'%s' % (self.id)
    class Meta:
        unique_together = ('node', 'date')
        db_table = settings.DB_PREFIX + 'data'
        verbose_name = _(u'Data')
        verbose_name_plural = _(u'Datas')
