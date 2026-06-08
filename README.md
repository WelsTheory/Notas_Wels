# Mis Posts

App web personal para guardar textos de posts que te gustan: el texto completo, el autor, el enlace de donde lo encontraste y etiquetas para organizarlos. Accesible desde cualquier dispositivo en tu red Tailscale, incluyendo iPhone.

## Funcionalidades

- **Guardar posts** — interfaz limpia para pegar el texto, agregar autor, enlace, fuente (Twitter, Instagram, LinkedIn, Blog, etc.) y etiquetas libres
- **Post aleatorio** — un botón que te muestra un post guardado al azar para releerlo
- **Buscador** — filtra por texto, autor, red social o etiqueta
- **Responsive** — diseño oscuro optimizado para móvil (iPhone) y escritorio

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

```bash
# 1. Clona el repositorio
git clone <url-del-repo>
cd <nombre-del-repo>

# 2. Crea y activa el entorno virtual
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Configura las variables de entorno
cp .env.example .env
```

Abre el archivo `.env` y reemplaza el valor de `SECRET_KEY` por una clave nueva. Puedes generar una con:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

```bash
# 5. Crea la base de datos
python manage.py migrate

# 6. Arranca la app
./start.sh          # Linux / macOS
# python manage.py runserver 0.0.0.0:8080   # alternativa en cualquier OS
```

La app queda disponible en `http://localhost:8080`.

## Acceso vía Tailscale

Desde cualquier dispositivo conectado a tu red Tailscale, abre:

```
http://<IP-Tailscale-de-tu-máquina>:8080
```

No requiere login — el acceso está controlado por Tailscale.

## Panel de administración (opcional)

Django incluye un admin para gestionar posts y etiquetas directamente:

```bash
python manage.py createsuperuser
```

Disponible en `http://localhost:8080/admin/`.

## Stack

- [Django](https://www.djangoproject.com/) + SQLite3
- [Tailwind CSS](https://tailwindcss.com/) (CDN)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
