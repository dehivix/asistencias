import base64
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from asistencia.models import Asistencia, Profesores


@require_GET
def escanear(request):
    """Renderiza la página del escáner QR."""
    return render(request, "asistencia/escanear.html")


@require_POST
def registrar_asistencia(request):
    """Recibe el contenido raw del QR, decodifica la cédula y registra asistencia."""
    try:
        body = json.loads(request.body)
        qr_data = body.get("qr_data", "")
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"ok": False, "error": "Datos inválidos."}, status=400)

    if not qr_data:
        return JsonResponse({"ok": False, "error": "No se recibió código QR."}, status=400)

    # Decodificar base64 x9 (mismo proceso que el encode en Profesores.save)
    cedula = qr_data
    try:
        for _ in range(9):
            cedula = base64.b64decode(cedula).decode("utf-8")
    except Exception:
        return JsonResponse({"ok": False, "error": "Código QR no válido."}, status=400)

    # Buscar profesor por cédula
    try:
        cedula_int = int(cedula)
    except ValueError:
        return JsonResponse({"ok": False, "error": "Cédula no válida."}, status=400)

    profesor = Profesores.objects.filter(personas__cedula=cedula_int, activo=True).select_related("personas").first()

    if not profesor:
        return JsonResponse({"ok": False, "error": "Profesor no encontrado o inactivo."}, status=404)

    # Registrar asistencia
    asistencia = Asistencia.objects.create(profesor=profesor)

    return JsonResponse({
        "ok": True,
        "nombre": str(profesor.personas),
        "entrada": asistencia.entrada.strftime("%d/%m/%Y %H:%M:%S"),
    })
