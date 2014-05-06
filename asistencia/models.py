from django.db import models
import os
import shutil
import base64
from lib.qrtools  import QR

class Personas(models.Model):
    cedula = models.BigIntegerField()
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    sexo = models.CharField(max_length=10,choices=(('masculino','Masculino'),('femenino','Femenino')))
    correo = models.EmailField(max_length=75)
    telefono = models.BigIntegerField()
    class Meta:
        db_table='personas'
        verbose_name_plural='Personas'
    def __unicode__(self):
        return "%s %s" % (self.nombre,self.apellido)

class Materias(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    class Meta:
        db_table='materias'
        verbose_name_plural='Materias'
    def __unicode__(self):
        return "%s-%s" % (self.codigo,self.nombre)

class Profesores(models.Model):
    personas = models.ForeignKey(Personas,unique=True)
    materias = models.ManyToManyField(Materias)
    activo = models.BooleanField(default=True)
    codigo_qr = models.ImageField(max_length=50, blank=True, null=True,  verbose_name="Codigo Qr", help_text='ESTE CODIGO SE GENERARA AUTOMATICAMENTE y para descargarlo presione el click derecho del mouse sobre el enlace con la ruta, luego "guargar como", y a continuacion seleccione la carpeta de destino (solo si posee los permisos)', upload_to="qr/")
    def get_materias(self):
        return ', '.join([a.nombre for a in self.materias.all()])    
    get_materias.short_description = 'Materias'  
    get_materias.admin_order_field = 'materias__nombre'   
    class Meta:
        db_table='profesores'
        verbose_name_plural='Profesores'
        ''' Agregando permiso para que un usuario pueda descargar los qr '''
        permissions=(('descargar_qr','Descargar los codigos qr'),)
    def __unicode__(self):
        return "%s" % (self.personas)

    ''' Reescribiendo la funcion de guardado para generar QR al crear el profesor '''
    def save(self,*args,**kwargs):
        cedula=str(self.personas.cedula)
        nombre=cedula
        for i in range(1,10):
            cedula=base64.b64encode(cedula)
        code = QR(data=cedula, pixel_size=10)
        code.encode()
        src = code.get_tmp_file()
        dst = '%s/qr/%s.png'%(os.getcwd(),nombre)
        shutil.copy(src, dst)
        self.codigo_qr = dst

        super(Profesores,self).save(*args,**kwargs)

class Asistencia(models.Model):
    profesor = models.ForeignKey(Profesores)
    entrada = models.DateTimeField(auto_now=True,blank=True)
    salida = models.DateTimeField(auto_now=True,blank=True)
    class Meta:
        db_table='asistencia'
        verbose_name_plural='Asistencia'
    def __unicode__(self):
        return "%s " % (self.profesor)
