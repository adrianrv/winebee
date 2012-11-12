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

import time
import serial
import urllib2

# Cadena de ejemplo que recibimos de un mote cualquiera
#@2|689|data0-864|data1-551|data2-161#

# Dirección de la aplicación web donde debe enviar los datos
BASE_URL = 'http://winebee.aquicomo.com/'
# Puerto usb donde está conectado el gateway
ser = serial.Serial('/dev/ttyACM0', 9600)

# Programa principal se ejecuta indefinidamente
while 1:
    # Leemos datos del serial (usb)
    data = ser.readline()
    # Imprimimos los datos que hemos leido en la pantalla
    print data
    # Separamos el texto delimitado por el caracter |
    data = data.split('|')
    # Comprobar que tenemos 5 datos en el vector:
    # (mote-modulo, contador de datos, lum, hum, temp)
    if (len(data) == 5):
        # Quitamos la @ del identificador del mote
        mod = data[0].split('@')[1]
        # obtenemos el contador del datos (siempre en aumento)
        cont = data[1]
        # obtenemos la luminosidad quitando data-0
        lum = data[2].split('-')[1]
        # obtenemos la humedad quitando data-1
        hum = data[3].split('-')[1]
        # obtenemos la temperatura quitando data-2 y quitando el # del final
        temp = data[4].split('-')[1].split('#')[0]
        # hacemos la conversión diviendo el dato por 10 para pasar a grados
        temp = str(float(temp) / 10)
        # Imprimimos en pantalla los datos que hemos recogido
        print 'Modulo ' + mod
        print 'Dato: ' + cont
        print 'Temperatura: ' + temp
        print 'Humedad: ' + hum
        print 'Luminosidad: ' + lum
        # Contruimos la dirección web donde debemos enviar los datos
        url = BASE_URL + '?node=' + mod + '&temp=' + temp + '&hum=' + hum + '&lum=' + lum
        # Hacemos el envío de los datos a esta dirección
        try:
            # y almacenamos la respuesta del servidor en la variable res
            res = urllib2.urlopen(url).read()
            # si es un OK todo ha ido bien y el dato queda almacenado
            if res == 'OK':
                # Imprimirmos en pantalla el mensaje OK
                print 'Dato almacenado.'
            else:
                # Si no recibimos un OK, es que puede haber un error de comunicación
                print 'Error al amacenar dato!'
        except:
            # Ha habido un error, no hemos podido conectar
            print 'Error al amacenar dato!'
        print ''

