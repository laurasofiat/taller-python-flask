# MANEJO DE EXCEPCIONES---------------------------------------------

try: #bloque de codigo que podria tener error en int
    nom=input("Hola usuario ingresa tu nombre: ")
    ex=int(input("Ingresa cualquier número para sacar su cubo: "))
    c=ex**3
    print(f"{nom} el cubo de {ex} es: {c}")
except ValueError: #bloque que imprime un mensaje al tener un dato incorrecto
    print("El número ingresado debe ser un entero no un decimal.")
finally: #bloque que imprime mensaje sin importar resultados anteriores
    print(f"Adiós {nom}.")
    

try: 
    print(f"Hola {nom}. Esta vez multiplicaremos 99 por un número, para que adivines cuál da como resultado 6732. \n !Ánimo!") #explicacion
    n=float(input("Ingresa un número: ")) #interacion para meter numero correcto
    while n!=68: #ientras que el numero ingresado sea diferente de 68, se ejecuta el siguiente bloque
        print(f"Estas mal en matemáticas {nom}. Piensa mejor") #mensaje de aliento
        n=float(input("Intenta de nuevo: ")) #interacion para repetir el proceso hasta que el numero ingresado sea 68
    print(f"La pensaste muy bien {nom} , el número que ingresaste es: {n}.") #mensaje de felicitación
except ValueError: #bloque que imprime un mensaje al tener un dato incorrecto
    print("Debes ingresar un número en dígito, no escrito.")
except ZeroDivisionError: #bloque que imprime un mensaje al tener un error de división entre cero
    print("No puedes dividir entre cero.")
finally:    
    print(f"Adiós {nom}. Mejora tus matemáticas, no te desanimes, sigue practicando.")


p=input("Deseas seguir prácticando para mejorar? (si/no). ").lower() #interacción para continuar practicando
while p=="si": #mientras se desee practicar
    try: #bloque de codigo que podria tener error en int
        print(f"{nom}. Esta vez multiplicaremos el número 99 por otro número.Tendrás que adivinar su resultado \n !Ánimo!") #explicacion
        i=float(input("¿cuánto es 99 x 37: "))  #interacion para meter numero correcto
        while i!=3663: #mientras que el numero ingresado sea diferente de 3663, se ejecuta el siguiente bloque
            print(f"Incorrecto. Estas mal en matemáticas {nom}.") #mensaje de aliento
            i=float(input("Intenta otra vez: ")) #interacion para repetir el proceso hasta que el numero ingresado sea 3663
        print("Correcto, ya estas mejorando tus matemáticas.") #mensaje de felicitación
        i1=float(input("¿cuánto es 99 x 88: ")) #interacion para meter numero correcto
        while i1!=8712: #mientras que el numero ingresado sea diferente de 8712, se ejecuta el siguiente bloque
            print(f"Incorrecto. Estas mal en matemáticas {nom}.") #mensaje de aliento
            i1=float(input("Intenta otra vez: ")) #interacion para repetir el proceso hasta que el numero ingresado sea 8712
        print("Correcto, ya estas mejorando tus matemáticas.") #mensaje de felicitación
        i2=float(input("¿cuánto es 99 x 43: "))  #interacion para meter numero correcto
        while i2!=4257: #mientras que el numero ingresado sea diferente de 4257, se ejecuta el siguiente bloque
            print(f"Incorrecto. Estas mal en matemáticas {nom}.") #mensaje de aliento
            i2=float(input("Intenta otra vez: ")) #interacion para repetir el proceso hasta que el numero ingresado sea 4257
        print("Correcto, ya estas mejorando tus matemáticas.") #mensaje de felicitación
        p=input("Deseas repetir el proceso? (si/no). ").lower() #interacción para continuar practicando
    except ValueError: #bloque que imprime un mensaje al tener un dato incorrecto
        print("Debes ingresar un número en dígito, no escrito.")
    finally:    #bloque que imprime mensaje sin importar resultados anteriores
        print(f"Adiós {nom}. ")
        
#En esta la pense mucho para que código dinamico poner, como se multiplicar cualquier numer del 1 al 100 por 99 pense que seria divertido
