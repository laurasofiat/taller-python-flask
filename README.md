# Taller de Python y Flask

## Descripción
Este proyecto reúne los ejercicios y el desarrollo práctico del taller de Python y Flask. Durante su desarrollo se trabajaron los fundamentos del lenguaje Python, el desarrollo de aplicaciones web con Flask, el uso de bases de datos SQLite, el manejo de Git y GitHub, y la organización de un proyecto final que integra todos los temas vistos.

Cada parte del taller fue construida de forma progresiva: primero lo básico de Python, luego Flask, después la conexión con SQLite, y por último un proyecto completo aplicando todo lo aprendido.

## Temas desarrollados

### Python
- Variables y tipos de datos.
- Condicionales.
- Ciclos (while y for).
- Funciones.
- Listas, tuplas y diccionarios.
- Manejo de archivos.
- Manejo de excepciones.
- Programación Orientada a Objetos (POO).

### Flask
- Intalación.
- Rutas .
- Plantillas HTML con Jinja2.
- Formularios HTML con método POST y GET.
- Variables de URL y parámetros de consulta.
- Archivos estáticos (CSS).
- Herencia de plantillas.
- Redireccionamiento y uso de `url_for()`.
- Manejo de errores 404 y 500.
- Sesiones.
- API REST con respuestas JSON.

### Bases de datos
- SQLite con Python.
- Integración de Flask con SQLite (CRUD básico).

### Herramientas de desarrollo
- Entornos virtuales (`venv`).
- Git y GitHub.
- Archivo `.gitignore`.
- Documentación con `README.md`.

## Tecnologías utilizadas
- Python 3
- Flask
- SQLite
- HTML5
- CSS3
- Jinja2
- Git
- GitHub
- Visual Studio Code

## Estructura del proyecto

```text
taller-python-flask/
│
├── part1_python/
│   ├── variables.py
│   ├── condicionales.py
│   ├── ciclos.py
│   ├── Funciones.py
│   ├── Listas,tuplas,diccionarios.py
│   ├── Manejo_archivos.py
│   ├── Manejo_excepciones.py
│   └── POO.py
│
├── part2_python/
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── base_hijo.html
│   │   ├── index.html
│   │   └── registro.html
│   └── static/
│       └── index.css
│
├── part3_python/
│   ├── sqlite.py
│   ├── sqlite_flask.py
│   ├── templates/
│   │   └── registros.html
│   ├── info.txt
│   └── usuarios.db
│
├── final_proyect/
│   ├── app.py
│   ├── cultura.db
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── agregar.html
│   │   └── catalogo.html
│   └── static/
│       └── style.css
│
└── .gitignore
```

## Instalación

1. Clonar el repositorio.

```bash
git clone https://github.com/laurasofiat/taller-python-flask.git
```

2. Crear un entorno virtual.

```bash
python -m venv venv
```

3. Activar el entorno virtual.

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

4. Instalar Flask.

```bash
python -m pip install flask
```

5. Ejecutar la aplicación deseada (desde su carpeta correspondiente).

```bash
python part2_python/app.py

python part3_python/sqlite_flask.py

python final_proyect/app.py

```

## Proyecto final: Patrimonio Cultural Colombiano

El proyecto final, ubicado en `final_proyect`, es un catálogo que permite registrar elementos culturales que representan y resaltan a colombia: fiestas, danzas, gastronomía, música, artesanías y sitios arqueológicos, clasificados por región. Cuenta con tres rutas (inicio, agregar y catálogo), un formulario con validación, y una base de datos SQLite donde se guarda toda la información.

## Objetivo
El objetivo de este proyecto es el trabajo que fortalece los conocimientos fundamentales de Python y Flask mediante el desarrollo de ejemplos prácticos, comprendiendo el funcionamiento de aplicaciones web, el manejo de bases de datos y el control de versiones con Git.

## Autor
Laura Sofía Torres Murillo.
