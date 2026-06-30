import sqlite3 #se importa la libreria para bd

#base de datos ---------------------------------------------------------------------------------------------------------------

conn = sqlite3.connect("usuarios.db") #define conn que conectan o crean colegio.bd

cursor = conn.cursor() #crea un objeto para ejcutar bd

#cursor.execute ejecuta si la tabla no existe
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS registros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  
        nombre TEXT NOT NULL,               
        nota REAL NOT NULL                      
    )
""") #real es float

# Los signos ? son marcadores de posición seguros
cursor.execute("INSERT INTO registros (nombre, nota) VALUES (?, ?)", ("Ana", 90)) # se reemplaza el primer ? por Ana y el segundo por 90
cursor.execute("INSERT INTO registros (nombre, nota) VALUES (?, ?)", ("Luis", 75))

conn.commit() #guarda cambios

resultados = cursor.execute("SELECT * FROM registros").fetchall() # se ejecuta la consulta y se obtienen todos los resultados
for fila in resultados:
    print(fila)     

uno = cursor.execute("SELECT * FROM registros WHERE id = ?", (1,)).fetchone() # se ejecuta la consulta y se obtiene el primer resultado
print(uno)

conn.close() #cierra la conexión



