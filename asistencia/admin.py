from django.contrib import admin
from asistencia.models import Asistencia, Materias, Personas, Profesores


class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("profesor", "entrada", "salida")
    search_fields = ("profesor__personas__nombre", "profesor__personas__apellido")


admin.site.register(Asistencia, AsistenciaAdmin)


class MateriasAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre")
    search_fields = ("codigo", "nombre")


admin.site.register(Materias, MateriasAdmin)


class PersonasAdmin(admin.ModelAdmin):
    list_display = ("cedula", "nombre", "apellido")
    search_fields = ("cedula", "nombre", "apellido")
    list_filter = ("sexo",)


admin.site.register(Personas, PersonasAdmin)


class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ("personas", "get_materias", "activo")
    search_fields = ("personas__nombre", "personas__apellido")
    list_filter = ("materias", "activo")

    # chequeando permisos para descargar los qr
    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            if not request.user.has_perm("asistencia.descargar_qr"):
                return self.readonly_fields + ("codigo_qr",)
        return self.readonly_fields


admin.site.register(Profesores, ProfesoresAdmin)
