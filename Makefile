.PHONY: build up down logs migrate makemigrations createsuperuser test shell bash lint check collectstatic help

# ---------------------------------------------------------------------------
# DOCKER
# ---------------------------------------------------------------------------
build:
	@echo "\033[1;33m🔨 Construyendo imagen...\033[0m"
	docker compose build

up:
	@echo "\033[1;32m🚀 Levantando el entorno...\033[0m"
	docker compose up -d
	@echo "\033[1;32m✅ Disponible en http://localhost:8000/admin/\033[0m"

down:
	@echo "\033[1;34m🛑 Deteniendo contenedores...\033[0m"
	docker compose down --remove-orphans

logs:
	@echo "\033[1;34m📜 Mostrando logs...\033[0m"
	docker compose logs --tail=100 -f

restart:
	@echo "\033[1;34m🔄 Reiniciando...\033[0m"
	docker compose restart

rebuild: down build up

# ---------------------------------------------------------------------------
# DJANGO
# ---------------------------------------------------------------------------
migrate:
	@echo "\033[1;32m🛠️  Aplicando migraciones...\033[0m"
	docker compose exec django python manage.py migrate

makemigrations:
	@echo "\033[1;33m📦 Generando migraciones...\033[0m"
	docker compose exec django python manage.py makemigrations

createsuperuser:
	@echo "\033[1;33m👤 Creando superusuario...\033[0m"
	docker compose exec django python manage.py createsuperuser

test:
	@echo "\033[1;34m🧪 Ejecutando tests...\033[0m"
	docker compose exec django python manage.py test

check:
	@echo "\033[1;32m✅ Ejecutando check de Django...\033[0m"
	docker compose exec django python manage.py check

shell:
	@echo "\033[1;34m🐚 Abriendo shell de Django...\033[0m"
	docker compose exec django python manage.py shell

bash:
	@echo "\033[1;34m🐚 Accediendo al contenedor...\033[0m"
	docker compose exec django bash

collectstatic:
	@echo "\033[1;34m🗂️  Recolectando archivos estáticos...\033[0m"
	docker compose exec django python manage.py collectstatic --noinput

lint:
	@echo "\033[1;34m🔍 Ejecutando linter...\033[0m"
	docker compose exec django python -m py_compile manage.py
	docker compose exec django python -m py_compile Asistencias/settings.py
	docker compose exec django python -m py_compile Asistencias/urls.py
	docker compose exec django python -m py_compile asistencia/models.py
	docker compose exec django python -m py_compile asistencia/admin.py
	@echo "\033[1;32m✅ Sin errores de sintaxis.\033[0m"

# ---------------------------------------------------------------------------
# HELP
# ---------------------------------------------------------------------------
help:
	@echo ""
	@echo "\033[1;35m📋 COMANDOS DISPONIBLES\033[0m"
	@echo ""
	@echo "\033[1;32m  Docker:\033[0m"
	@echo "    make build            - Construir imagen Docker"
	@echo "    make up               - Levantar entorno"
	@echo "    make down             - Detener entorno"
	@echo "    make logs             - Ver logs"
	@echo "    make restart          - Reiniciar contenedores"
	@echo "    make rebuild          - Reconstruir todo"
	@echo ""
	@echo "\033[1;33m  Django:\033[0m"
	@echo "    make migrate          - Aplicar migraciones"
	@echo "    make makemigrations   - Generar migraciones"
	@echo "    make createsuperuser  - Crear superusuario"
	@echo "    make test             - Ejecutar tests"
	@echo "    make check            - Django system check"
	@echo "    make shell            - Shell de Django"
	@echo "    make bash             - Bash en contenedor"
	@echo "    make collectstatic    - Recolectar estáticos"
	@echo "    make lint             - Verificar sintaxis"
	@echo ""
