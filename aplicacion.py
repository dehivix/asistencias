#!/usr/bin/env python
"""
Aplicación de lectura de QR por webcam para registro de asistencias.

NOTA: Esta aplicación requiere una webcam y la librería pyzbar instalada.
Es funcionalidad opcional — el sistema de admin web funciona sin ella.
"""
import os
import sys
import base64

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Asistencias.settings")

import django

django.setup()

from asistencia.models import Profesores, Asistencia

"""
    @TODO:
        # Hacer que la aplicacion corra sobre gtk, sin interacciones de consola, solo dar la 
        bienvenida 3 segundos y seguir registrando las entradas
        
        # Guardar entradas y salidas segun sea el caso y no el autonow del modelo

        # Mejorar la logica de las entradas/salidas, por ejemplo, normar las horas por la app
        del administrador

"""

print("NOTA: La funcionalidad de webcam requiere pyzbar y una cámara conectada.")
print("Esta aplicación es opcional. Usa el admin web en http://localhost:8000/admin/")

# Webcam QR reading would go here if pyzbar + camera are available.
# For now, this script accepts manual input for testing.
while True:
    cod = input("Ingrese la cédula del profesor (o 'salir' para terminar): ")
    if cod.lower() == "salir":
        break
    try:
        profesor = Profesores.objects.filter(personas__cedula=int(cod))
        if profesor.exists():
            asistencia = Asistencia.objects.create(profesor=profesor[0])
            print(
                "Bienvenido %s %s"
                % (profesor[0].personas.nombre, profesor[0].personas.apellido)
            )
            print("Entrada guardada:", asistencia.entrada)
        else:
            print("Profesor no existe")
    except ValueError:
        print("Cédula inválida, intente de nuevo.")
    input("Presione enter para continuar...")
    os.system("clear")
