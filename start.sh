#!/bin/bash
# Script para iniciar Mis Posts en el puerto 8005
cd "$(dirname "$0")"

echo "Iniciando Mis Posts..."
echo "================================"

# Activar entorno virtual
source venv/bin/activate

# Verificar que el entorno virtual está activado
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Error: No se pudo activar el entorno virtual"
    exit 1
fi

echo "Entorno virtual activado"

# Instalar/actualizar dependencias
echo ""
echo "Verificando dependencias..."
pip install -r requirements.txt --quiet
echo "Dependencias actualizadas"

# Ejecutar migraciones
echo ""
echo "Aplicando migraciones de base de datos..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Error al aplicar migraciones"
    exit 1
fi
echo "Migraciones aplicadas correctamente"

# Recolectar archivos estáticos
echo ""
echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput --clear
echo "Archivos estáticos recolectados"

# Obtener IP de Tailscale
echo ""
echo "Buscando IP de Tailscale..."
TAILSCALE_IP=$(ip addr show tailscale0 2>/dev/null | grep "inet " | awk '{print $2}' | cut -d/ -f1)

if [ -z "$TAILSCALE_IP" ]; then
    echo "No se detectó IP de Tailscale. El servidor estará accesible solo en localhost."
    echo "   Si quieres acceso remoto, asegúrate de que Tailscale esté corriendo."
else
    echo "IP de Tailscale detectada: $TAILSCALE_IP"
fi

# Iniciar servidor
echo ""
echo "================================"
echo "Servidor ejecutándose en:"
echo "   - Local:     http://localhost:8005"
echo "   - Red:       http://0.0.0.0:8005"
if [ -n "$TAILSCALE_IP" ]; then
    echo "   - Tailscale: http://$TAILSCALE_IP:8005"
fi
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo "================================"
echo ""

python manage.py runserver 0.0.0.0:8005
