#!/bin/sh
# Script que permite la instalacion de las aplicaciones necesarias
#Ejecutar en modo root

exec su -c "

echo 'Comenzando la instalacion de las dependencias basicas';
aptitude install sqlite3; 
aptitude install qrencode; 
aptitude install python-zbar; 

echo 'Preparando para instalar setup tools. (Ejecuciones de pip install)';
aptitude install python-pip; 

echo 'Preparando para instalar ReportLab. (Para los reportes en PDF)';
aptitude install python-reportlab;

echo 'Terminada la instalación de aplicaciones. Comenzando actualización de Django...';
pip install --upgrade django==1.5.4;

echo 'Preparando para instalar django-admin-bootstrapped (mejoras al entorno)';
pip install django_admin_bootstrapped;

echo 'Terminada la instalacion de las dependencias, es hora de probar la app';

"
