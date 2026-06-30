from flask import Flask, request, redirect, url_for, render_template #importa flask y dependencias
import sqlite3 #importa sql para bd
import os #se usa para construir la ruta absoluta de la bd

app = Flask(__name__) #crea 
app.secret_key = "claveultrasecreta" #clave secreta para session

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cultura.db") #ruta absoluta de la bd, evita que se cree en otra carpeta

def conectar(): #funcion para conectar
    conn = sqlite3.connect(DB) #crea o abre la base de datos
    conn.row_factory = sqlite3.Row #acede a la columnas de la base de datos 
    return conn #se devuelve al cursor

def iniciar_bd(): #funcion iniciar
    conn = conectar() #conecta a la base de datos
    conn.execute(""" 
        CREATE TABLE IF NOT EXISTS culturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            region TEXT NOT NULL,
            tipo TEXT NOT NULL,
            descripcion TEXT NOT NULL
        )
    """)#crea la base de datos i no existe la tabla
    conn.commit() #guarda datos
    conn.close() #cierra coneixon

iniciar_bd() #

@app.route("/") #ruta principal
def index(): #funcion index
    conn = conectar() #conecta a la bd
    total = conn.execute("SELECT COUNT(*) AS total FROM culturas").fetchone()["total"] #selecciona todo de culturas
    conn.close() #cierra cursor
    return render_template("index.html", titulo="La Cultura Colombiana", total=total) #devuelve a index con titulo y cantidad de datos guardados

@app.route("/agregar", methods=["GET", "POST"]) #ruta agregar que obtiene o crea
def agregar():
    error = None  #se rellena el error y se deja en none cuando no hay que mostrar nada
    if request.method == "POST": #si el metodo es crear
        nombre = request.form.get("nombre") #define el nombre en diccionario
        region = request.form.get("region") #define region
        tipo = request.form.get("tipo") #tipo
        descripcion = request.form.get("descripcion") #descripcion

        if not nombre or not region or not tipo or not descripcion: #si no hay campos
            error = "Debes completar todos los campos." #mensaje de aviso
        else: #sino
            conn = conectar() #conecta a bd
            conn.execute( #ejecuta el insertar los datos
                "INSERT INTO culturas (nombre, region, tipo, descripcion) VALUES (?, ?, ?, ?)",
                (nombre, region, tipo, descripcion)
            )
            conn.commit() #guarda en el diccionario
            conn.close() #cierra conexion
            return redirect(url_for("catalogo")) #redirige a catalogo

    return render_template("agregar.html", error=error) #si no es crear redirige agregar

@app.route("/catalogo") #ruta catalogo
def catalogo(): #funcion
    conn = conectar() #conecta abd
    culturas = conn.execute("SELECT * FROM culturas ORDER BY region").fetchall() #selecciona todo de bd por orden de bd
    conn.close() #cierra conexion
    return render_template("catalogo.html", culturas=culturas) #redirige a catalogo con info

if __name__ == "__main__":
    app.run(debug=True) #core app
