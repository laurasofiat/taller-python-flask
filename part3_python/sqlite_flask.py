#sqlite y flask----------------------------------------------------------------------------------------------------

import sqlite3 #se importa la libreria para bd
from flask import Flask, render_template, redirect, url_for, request #se importa flask y render_template para renderizar html y request para recibir datos del formulario

app = Flask(__name__) #se crea con flask el app

@app.route('/')
def registro():
    return redirect(url_for('registros'))

def conectar(): #funcion conectar
    conn = sqlite3.connect("usuarios.db") #coecta a la base de datos usuarios.db
    conn.row_factory = sqlite3.Row   #permite acceder a las columnas por nombre
    return conn #devuelve la conexion


@app.route("/registros", methods=["GET","POST"]) #ruta registros que 
def registros(): #funcion registro
    conn = conectar() #conecta a la base de datos
    cursor = conn.cursor() #se crea un cursor para ejecutar consultas

    #crear --------------------------------------------------------------------------------
    if request.method == "POST": #si el metodo es post 
        nombre = request.form.get("nombre") #se obtiene el nombre del formulario
        nota = request.form.get("nota") #se obtiene la nota del formulario
        cursor.execute( #se ejecuta la consulta para insertar los datos en la tabla registros
            "INSERT INTO registros(nombre,nota) VALUES(?,?)",
            (nombre, nota)
        )
        conn.commit() #guarda cambios

    #leer---------------------------------------------------
    cursor.execute("SELECT * FROM registros") #se ejecuta la consulta para obtener todos los registros de la tabla registros
    datos = cursor.fetchall() #obtiene todos los registros de la consulta
    conn.close() #cierra la conexion

    return render_template("registros.html", datos=datos) #redige a registro.html y envia los datos obtenidos de la base de datos

if __name__=='__main__':
    app.run(debug=True)
