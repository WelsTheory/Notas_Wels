#!/bin/bash
# Arranca la app en el puerto 8080 (accesible via Tailscale)
cd "$(dirname "$0")"
source venv/bin/activate
python manage.py runserver 0.0.0.0:8080
