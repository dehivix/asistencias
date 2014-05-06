### La siguiente aplicacion es un control de asistencias por medio de un codigo QR de contenido cifrado para el personal
# del Area de Ingenieria en Sistemas de la Universidad Nacional Experimental Romulo Gallegos, utilizando herramientas
# 100% software libre. ###

* Requerimientos:
 > django
 > sqlite3
 > django_admin_bootstrapped 
 > python-zbar
 > qrencode

* Instalacion:
- hemos creado un instalador para asegurarnos de que todas las dependencias necesarias estan disponibles en el sistema
para hacer uso de el solo basta con correrlo de la siguiente manera: 

`$ sh instalador.sh` 

te pedira la clave de root e instalara todo lo necesario (si desea puede instalar las dependencias por usted mismo).

* Uso:
------

   __aplicacion de asistencias:__
 	para el uso de la asistencia se debe correr el script "aplicacion.py" el cual mostrara la camara y la mantendra de tal forma
	para que al marcar la entrada, de la bienvenida y vuelva a esperar que los usuarios continuen marcando sus entradas.


   __aplicacion del administrador:__
	para la gestion y control de las asistencias se uso el admin de django, siendo ella una plataforma web de muy facil gestion,
	solo se debe correr el script "manage.py" de la siguiente manera:

`$ python manage.py runserver`

 	luego abrir el navegador en la ruta `http://localhost:8000/admin/` , el usuario es admin y la clave tambien es admin.

   __generador de codigos QR:__
	para generar los codigos qr de cada profesor se utiliza su cedula por ser un valor unico que no se repite, por lo tanto
	al crear el profesor desde el admin se creara automaticamente la imagen ( el qr) en el directorio de nombre "qr" cuyo nombre 
	es la cedula del profesor con extension .png
