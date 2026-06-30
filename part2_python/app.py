#FLASK-----------------------------------------------------------------------------------------

from flask import Flask, request,redirect, url_for, render_template,session, jsonify

app = Flask(__name__) #se define app acreando con flask para hcer el servidor

app.secret_key="clavesercreta" #<- clave secreta para session 

# ejemplo RUTAS--------------------------------------------------------------------------------------------
# @app.route('/casa') 
# def casa(): #funcion casa
#     return f"Esta es la ruta del casa" #imprime mensaje

# @app.route('/inicio') #ruta de inicio
# def inicio():
#     return f"Esta es la ruta de inicio" #imprime emnsaje


#ejemplo VARIABLES Y METODOS-----------------------------------------------------------------------------------------
# @app.route("/usuario/<nom>") #variable con ruta nombre
# def usuario(nom): #funcion ususario con variable nombre
#     return f"El ususario se llama : {nom}</p>" #devuelve mensaje con vatiable

# @app.route("/datos", methods=["GET", "POST"]) #ruta datos con metodo para obtener,crear
# def datos(): #duncion datos
#     return "Envía datos aquí"


#HTML con jinja2-----------------------------------------------------------------------------------------------------
@app.route('/') #ruta index
def index():
    contenido=[ #lista que almacena tiene definida la infortmacion de la ruta
        {'subtitulo': "Subtitulo de Pagina principal", #diccionario 
        'texto':'Aquí van parrafos de la pagina principal'}
    ]
    return render_template('index.html',contenido=contenido,titulo="Pagina principal") #redirige a carpeta templates buscando el archivo index.tml y se para la variable con argumento 

#HTML Y POST--------------------------------------------------------------------------------------

@app.route("/registro", methods=["GET", "POST"]) #ruta cregistro que utiliza metodos obtener y crear
def registro(): #funcion registro
    if request.method == "POST": #si en el registro la peticion es crear 
        nombre = request.form.get("nombre") #en la variable nombre se guarda un diccionario del registro - .get() hace que devuelva none si falla
        email = request.form.get("email") #en la variable email se guarda en el diccionario del registro
        return f"Nombre: {nombre} - Email: {email}"

    return render_template("registro.html") #Si la petición es GET se muestra el formulario vacío

#Variables de url y parametros de consulta-------------------------------------------------------------------------------------------

@app.route("/usuario/<int:id>") #ruta para identificar al usuario con id=42
def ver_usuario(id): 
    return f"<h2>Usuario número: {id}</h2>" #mensaje que devuelve el id del usuario

# Parámetros de consulta: /buscar?q=python&pagina=2
# Van después del ? y se leen con request.args.get()
@app.route("/buscar")
def buscar():
    info = request.args.get("q", "")   # " " es el valor por defecto si el parámetro no existe
    pagina = request.args.get("pagina", 1, type=int) # type=int convierte automáticamente el valor a entero
    return f"Buscando: {info} - Página: {pagina}" #mensaje 

#archivos estaticos-----------------------------------------------------------------------------------------------------------------------------
#ejemplo en index y registro

# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset="utf-8">
#         <meta http-equiv="X-UA-Compatible" content="IE=edge">
#         <title></title>
#         <meta name="description" content="">
#         <meta name="viewport" content="width=device-width, initial-scale=1">
#         <link rel="stylesheet" href="{{ url_for('static', filename='index.css') }}"> <- ahí--------------------------------------------------------------
#     </head>
#         <body>
#         {% if error %} <!--si da error-->
#             <p>{{ error }}</p> <!--muestra la variable definida en la funcion registro-->
#         {% endif %} <!--finaliza la condicion-->

#         <form method="POST" action="/registro"> <!--en el formulario se crea y envian los datos a la ruta registro-->
#             <input type="text" name="nombre" placeholder="Tu nombre" required> <!--name es el nombre de la clave de flask - en el campo de almacenaimeto debe ser llenado-->
#             <input type="email" name="email" placeholder="Tu email" required> 
#             <button type="submit">Registrar</button>
#         </form>
#     </body>
# </html>

#herencia de plantillas-------------------------------------------------------------------------------------------------------------

#archivo base.html--------------------------------------------------------------------------------
# <html>
#     <head>
#         <meta charset="utf-8">
#         <meta http-equiv="X-UA-Compatible" content="IE=edge">
#         <title>{% block titulo %}{% endblock %}</title>
#         <meta name="viewport" content="width=device-width, initial-scale=1">
#         <link rel="stylesheet" href="index.css">
#     </head>
#     <body>
#         {% block content %}{% endblock %} <!-- las páginas hijas insertan su contenido aquí -->
#     </body>
# </html>

#archivo base_hijos ---------------------------------------------------------
# {% extends "base.html" %} <!-- hereda la estructura de base.html -->

# {% block titulo %}Registro{% endblock %} <!-- rellena el <title> -->

# {% block content %} <!-- todo esto va dentro del <body> de base.html -->

#     {% if error %}
#         <p>{{ error }}</p>
#     {% endif %}

#     <form method="POST" action="/registro">
#         <input type="text"   name="nombre" placeholder="Tu nombre" required>
#         <input type="email"  name="email"  placeholder="Tu email"  required>
#         <button type="submit">Registrar</button>
#     </form>

# {% endblock %}

@app.route("/base_hijo")
def base_hijo():
    return render_template("base_hijo.html")

#redireccionamiento y url---------------------------------------------------------------------------------------------------------------------

@app.route("/ir_index") #ruta 
def ir_index(): #funcion
    return redirect(url_for("index")) #redirige directamente a la intruccion en la funcion registro

#MANEJO DE ERRORES----------------------------------------------------------------------------------------

# Error 404: página no encontrada
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "<h2>Error 404 - Página no encontrada</h2>", 404

# Error 500: error interno del servidor
@app.errorhandler(500)
def error_servidor(error):
    return "<h2>Error 500 - Error interno del servidor</h2>", 500


#SESIONES----------------------------------------------------------------------------------------------

#Guardar información en la sesión
@app.route("/login")
def login():
    session["usuario"]="Laura"
    return "Sesión iniciada."

#Leer información guardada
@app.route("/perfil")
def perfil():
    usuario=session.get("usuario")
    return f"Bienvenido {usuario}"

#Cerrar sesión
@app.route("/logout")
def logout():
    session.pop("usuario",None)
    return "Sesión finalizada."

#API REST---------------------------------------------------------------------------------------------

#Endpoint que devuelve información en formato JSON
@app.route("/api/usuario")
def api_usuario():
    datos={
        "id":1, "nombre":"Laura", "edad":18}
    return jsonify(datos)


#Lista de usuarios
@app.route("/api/usuarios")
def api_usuarios():
    usuarios=[
        {"id":1,"nombre":"Laura"},
        {"id":2,"nombre":"Carlos"},
        {"id":3,"nombre":"Ana"}]

    return jsonify(usuarios)

# Para probar la API:
# En el navegador escribir:
# http://127.0.0.1:5000/api/usuario
#
# También puede probarse con Postman realizando una petición GET
# a la misma dirección para visualizar la respuesta en formato JSON.


if __name__=="__main__":  
    app.run(debug=True) # app.run inica el servidor y debug=true hace que se reinici el servidor al subir cambios


