#MANEJO DE ARCHIVOS-------------------------------------

with open("README.md", "w") as f: #cierra el archivo al terminar(with) la abertura de rEADME.md(open) que fue creado o sobrescritro(w) del archivo(f)
    f.write("Readme describe el app del taller\n")   #despues de abrir el archivo se escribe en el archivo con write() lo que se quiere escribir en el archivo

with open("README.md", "r") as f: #cierra el archivo al terminar(with) la abertura de rEADME.md(open) para leer(r) el archivo(f)
    for linea in f: #itera linea por linea del archivo
        print(linea) #imprime linea por linea de readme.md
        
with open("README.md", "a") as f: #cierra el archivo al terminar(with) la abertura de rEADME.md(open) para agregar al final sin borrar contenido existente(a) en el archivo(f)
    f.write("Readme tiene informacion del app\n") #escribe al final del archivo
    
    