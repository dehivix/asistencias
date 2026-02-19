# Asistencias

Control de asistencias por medio de código QR de contenido cifrado para el personal del Área de Ingeniería en Sistemas de la Universidad Nacional Experimental Rómulo Gallegos.

## Requisitos

- [Docker](https://docs.docker.com/get-docker/) y Docker Compose

## Quick Start

```bash
# 1. Copiar variables de entorno
cp .env.example .env

# 2. Construir y levantar
make build
make up

# 3. Crear superusuario
make createsuperuser

# 4. Acceder
# Admin:    http://localhost:8000/admin/
# Escáner:  http://localhost:8000/escanear/
```

## Uso

### Admin (`/admin/`)

Panel de administración para gestionar personas, profesores, materias y asistencias. Al crear un profesor se genera automáticamente su código QR a partir de la cédula.

### Escáner QR (`/escanear/`)

Interfaz web pública que usa la cámara del dispositivo (móvil o desktop) para leer el código QR de un profesor y registrar su asistencia automáticamente.

**Flujo:**

1. Abrir `http://localhost:8000/escanear/` en el navegador
2. Permitir acceso a la cámara
3. Apuntar al código QR del profesor
4. La asistencia se registra y muestra confirmación con nombre y hora
5. Tras 3 segundos, el escáner se reactiva automáticamente

### API de registro (`/api/registrar/`)

Endpoint POST que recibe el contenido raw del QR, decodifica la cédula (base64 ×9) y crea el registro de asistencia. Devuelve JSON:

```json
{ "ok": true, "nombre": "Nombre Apellido", "entrada": "19/02/2026 14:30:00" }
```

## Comandos disponibles

| Comando                | Descripción             |
| ---------------------- | ----------------------- |
| `make build`           | Construir imagen Docker |
| `make up`              | Levantar entorno        |
| `make down`            | Detener entorno         |
| `make logs`            | Ver logs                |
| `make restart`         | Reiniciar contenedores  |
| `make rebuild`         | Reconstruir todo        |
| `make migrate`         | Aplicar migraciones     |
| `make makemigrations`  | Generar migraciones     |
| `make createsuperuser` | Crear superusuario      |
| `make test`            | Ejecutar tests          |
| `make check`           | Django system check     |
| `make shell`           | Shell de Django         |
| `make bash`            | Bash en contenedor      |
| `make collectstatic`   | Recolectar estáticos    |
| `make lint`            | Verificar sintaxis      |
| `make help`            | Ver todos los comandos  |

## Stack

- **Python** 3.12
- **Django** 5.1 LTS
- **SQLite** (base de datos)
- **Docker** (contenerización)
- **qrcode** (generación de QR)
- **html5-qrcode** (lectura de QR desde cámara, CDN)
- **Tailwind CSS** (interfaz del escáner, CDN)

## Estructura del proyecto

```
asistencias/
├── Asistencias/          # Configuración Django (settings, urls, wsgi)
├── asistencia/           # App principal
│   ├── models.py         # Personas, Materias, Profesores, Asistencia
│   ├── admin.py          # Configuración del admin
│   ├── views.py          # Vistas: escáner QR + API de registro
│   ├── urls.py           # Rutas de la app
│   └── templates/        # Template del escáner QR
├── lib/                  # Utilidades (generador QR)
├── Dockerfile
├── docker-compose.yml
├── local.yml             # Docker Compose alternativo
├── Makefile
├── requirements.txt
└── .env.example
```

## Generación de códigos QR

Al crear un profesor desde el admin, se genera automáticamente su código QR usando la cédula como identificador único. La cédula se codifica 9 veces en base64 y se genera la imagen QR con la librería `qrcode`. Las imágenes se guardan en `media/qr/` y son descargables desde el admin.

## Desarrolladores

- Dehivis Pérez

**Institución:** Universidad Nacional Experimental Rómulo Gallegos
