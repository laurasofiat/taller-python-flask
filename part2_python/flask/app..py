#FLASK-----------------------------------------------------------------------------------------

from flask import Flask, render_template #de la importacion flask importeme render_template

app= Flask(__name__) #se define app acreando con flask para hcer el servidor

#RUTAS--------------------------------------------------------------------------------------------
@app.route('/casa') 
def casa(): #funcion casa
    return f"Esta es la ruta del casa" #imprime mensaje

@app.route('/inicio') #ruta de inicio
def inicio():
    return f"Esta es la ruta de inicio" #imprime emnsaje


#VARIABLES Y METODOS----------------------------------------------------------------------------------------
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
<h1>{{titulo}}</h1>  #pone en un titulo tamaño grande la variable titulo de la funcion index
{% for c in contenido%} #recorre la lista
    <li> #
        {% if contenido == " "%}
            {{c.subtitulo }}
            {{c.texto}}
    </li>

if __name__=="__main__": 
    app.run(debug=True) # app.run inica el servidor y debug=trur hace que se reinici el servidor al subir cambios


