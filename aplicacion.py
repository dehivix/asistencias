#!/usr/bin/env python
import os
import sys
import base64
from lib.qrtools  import QR

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Asistencias.settings")
from asistencia.models import *

'''
    @TODO:
        # Hacer que la aplicacion corra sobre gtk, sin interacciones de consola, solo dar la 
        bienvenida 3 segundos y seguir registrando las entradas
        
        # Guardar entradas y salidas segun sea el caso y no el autonow del modelo

        # Mejorar la logica de las entradas/salidas, por ejemplo, normar las horas por la app
        del administrador

'''

while True:
    codigo = QR() 
    codigo.decode_webcam()
    cod=codigo.data_encode[codigo.data_type](codigo.data)
    try:
        for i in range(1,10):
            cod=base64.b64decode(str(cod))
    except:
        print "Codigo QR Incorrecto..."
        cod='NULL'
    if cod == 'NULL':
        print "Error, no se reconoce bien el codigo qr, intente de nuevo!"
    else:
        profesor=Profesores.objects.filter(personas__cedula=cod)
        if profesor.exists():
            asistencia=Asistencia.objects.create(profesor=profesor[0])
            print "Bienvenido %s %s"%(profesor[0].personas.nombre,profesor[0].personas.apellido)
            print "entrada guardada: ",asistencia.entrada
        else:
            print "profesor no existe"
    raw_input("Presione enter para continuar...")
    os.system("clear")
