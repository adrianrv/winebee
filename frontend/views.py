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

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from models import *
from django.utils.translation import ugettext_lazy as _

def home(request):
    if request.GET.keys():
        if 'node' and 'temp' and 'hum' and 'lum' in request.GET.keys():
            node = request.GET.get('node')
            temp = float(request.GET.get('temp'))
            hum = request.GET.get('hum')
            lum = request.GET.get('lum')
            try:
                n = Node.objects.get(pk=node)
                d = Data (node=n, temperature=temp, humidity=hum, luminosity=lum)
                d.save()
                return HttpResponse('OK')
            except ObjectDoesNotExist:
                response = _('ERROR: Node %(node)s does not exists.') % { 'node': node }
                return HttpResponse(response)
            except:
                response = _('ERROR: Unknown error.') % {}
                return HttpResponse(response)
        else:
            response = _('ERROR: Incorrect parameters.') % {}
            return HttpResponse(response)
    else:
        sensors = dict()
        for n in Node.objects.all():
            sensors[n] = Data.objects.filter(node=n).order_by('-date')[:50]

    return render_to_response('frontend/index.html', {'sensors': sensors},
                               context_instance=RequestContext(request))
def showdata (request, id):
    node = get_object_or_404(Node, id=id)
    data = Data.objects.filter(node=node).order_by('-date')
    return render_to_response('frontend/showdata.html', {'node': node, 'data': data},
                            context_instance=RequestContext(request))
                            
def getdata (request, id=None):
    if id:
        data = Data.objects.filter(node=id).order_by('date')
        if data:
            return HttpResponse(data[0].temperatura)
        else:
            response = _('ERROR') % {}
            return HttpResponse(response)
    else:
        nodes = dict()
        for n in Node.objects.all():
            # The last 50 elements of every node
            nodes[n.id] = Data.objects.filter(node=n).order_by('date')[:1]
        
        res = ''
        for n in Node.objects.all():
            try:
                d = Data.objects.filter(node=n).order_by('-date')[:1][0]
                if d.temperature:
                    res += '%s %s %s %s ' % (n.id, d.temperature, d.humidity, d.luminosity)
                    res += d.date.strftime("%d %b %Y %H:%M:%S") + '|'
                else:
                    res += 'ERROR|'
            except IndexError:
                res += 'ERROR|'
        # Delete de last '|'
        res = res[:len(res)-1]
        return HttpResponse(res)
