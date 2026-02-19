from django.urls import path

from asistencia import views

urlpatterns = [
    path("", views.escanear, name="escanear"),
    path("api/registrar/", views.registrar_asistencia, name="registrar_asistencia"),
]
