venv/
__pycache__/
*.pyc
*.db
.env
.DS_Store

<!-- 

Explicación de cada elemento del archivo .gitignore
- venv/: ignora la carpeta del entorno virtual para no subir las librerías instaladas del proyecto, ya que cada usuario puede crear su propio entorno.
- __pycache__/: ignora la carpeta donde Python almacena archivos compilados para acelerar la ejecución del programa. Estos archivos se generan automáticamente.
- *.pyc: ignora todos los archivos compilados de Python con extensión .pyc, ya que no es necesario incluirlos en el repositorio.
- *.db: ignora las bases de datos con extensión .db, evitando subir información local o de prueba al repositorio.
- .env: ignora el archivo que almacena variables de entorno, como contraseñas, claves API y datos sensibles, para proteger la seguridad del proyecto.
- .DS_Store: ignora un archivo oculto creado automáticamente por macOS para almacenar información sobre la visualización de carpetas. No es necesario para el funcionamiento del proyecto. 
-->



