#FLASK-----------------------------------------------------------------------------------------

from flask import Flask,request, render_template #de la importacion flask importeme render_template

app= Flask(__name__) #se define app acreando con flask para hcer el servidor

#RUTAS--------------------------------------------------------------------------------------------
@app.route('/casa') 
def casa(): #funcion casa
    return f"Esta es la ruta del casa" #imprime mensaje

@app.route('/inicio') #ruta de inicio
def inicio():
    return f"Esta es la ruta de inicio" #imprime emnsaje


#VARIABLES Y METODOS-----------------------------------------------------------------------------------------
@app.route("/usuario/<nom>") #variable con ruta nombre
def usuario(nom): #funcion ususario con variable nombre
    return f"El ususario se llama : {nom}</p>" #devuelve mensaje con vatiable

@app.route("/datos", methods=["GET", "POST"]) #ruta datos con metodo para obtener,crear
def datos(): #duncion datos
    return "Envía datos aquí"


#HTML con jinja2-----------------------------------------------------------------------------------------------------
@app.route('/') #ruta index
def index():
    contenido=[ #lista que almacena tiene definida la infortmacion de la ruta
        {'subtitulo': "Subtitulo de Pagina principal"}, #diccionario 
        {'texto'='Aquí van parrafos de la pagina principal'}, #diccionario
    ]
    return render_template('index.html',contenido=contenido,titulo="Pagina principal") #redirige a carpeta templates buscando el archivo index.tml y se para la variable con argumento 

# templates/index--------

# <h1>{{titulo}}</h1>  #pone en un titulo tamaño grande la variable titulo de la funcion index
# {% for c in contenido%} #recorre la lista
#     <li> 
#         {% if contenido != " "%} #si esta vacio
#             {{c.subtitulo }} #muestra el subtitulo
#             {{c.texto}} #muestra el texto
#     </li>

#HTML Y POST--------------------------------------------------------------------------------------

@app.route("/registro", methods=["GET", "POST"]) #ruta cregistro que utiliza metodos obtener y crear
def registro(): #funcion registro
    if request.method == "POST": #si en el registro la peticion es crear 
        nombre = request.form.get("nombre") #en la variable nombre se guarda un diccionario del registro - .get() hace que devuelva none si falla
        email = request.form.get("email") #en la variable email se guarda en el diccionario del registro

        if not nombre or not email: #si no hay nombre o email
            return render_template("registro.html", error="Todos los campos son obligatorios")

    return render_template("registro.html") #Si la petición es GET se muestra el formulario vacío

# <body>
#     {% if error %} #si da error
#         <p>{{ error }}</p> #muestra la variable definida en la funcion registro
#     {% endif %} #finaliza la condicion
#
#     <form method="POST" action="/registro"> #en el formulario se crea y envian los datos a la ruta registro
#         <input type="text" name="nombre" placeholder="Tu nombre" required> #name es el nombre de la clave de flask - en el campo de almacenaimeto debe ser llenado
#         <input type="email" name="email" placeholder="Tu email" required> 
#         <button type="submit">Registrar</button>
#     </form>
# </body>

if __name__=="__main__":  
    app.run(debug=True) # app.run inica el servidor y debug=trur hace que se reinici el servidor al subir cambios


