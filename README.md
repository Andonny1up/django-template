# Django Template

<div align="center">
    <img src="https://static.djangoproject.com/img/logos/django-logo-negative.png" alt="Django Logo" width="200">
</div>

Plantilla para iniciar un proyecto con Django y tailwind css, asignando configuraciones necesarias para desplegar un sitio de administración.

## Tecnologias

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,nodejs,django,tailwind" />
  </a>
</p>

## Requisitos

- Python >= 3.10
- Node >= 20
  - tailwind css > 3.4.12

## Iniciar Django
- Clonar el repositorio.
- Crear un entorno virtual para python.
```bash
python -m venv venv
```
- Iniciar el entorno virtual (venv).
- Instalar las dependencias de python.
```bash
pip install -r requirements.txt
```
- Algunas dependencias son:
  - Django 5.1.1
  - Python Dotenv 1.0.1
  - Pillow 10.4.1

## Tailwind
Para usar tailwind css
 - Crear un archivo en "./src/input.css"
 - Copiar el sigiente codigo al archivo "input.css"
```css

@tailwind base;
@tailwind components;
@tailwind utilities;

```
- Para iniciar el proceso de compilación de tailwind css ejecutar
```bash
npm run build:css

```
Esto iniciara el comando de compilacion hacia "./dashboard/static/dashboard/css/main.css" puedes cambiar esta configuración en el archivo "package.json"
```bash
"scripts": {
  "build:css": "npx tailwindcss -i ./src/input.css -o ./dashboard/static/dashboard/css/main.css --watch"
}

```

> 📘 Información
>
> Visita la documentación de tailwind css si tienes alguna duda sobre el proceso.
## Creditos

<a href="https://github.com/andonny1up">
  <img src="https://github.com/andonny1up.png" alt="Andoni Barba" width="100" style="border-radius: 50%">
</a>

> 📘 Información
>
> Django template aun no esta finalizado.
