#CICLOS-----------------------------------------------------------------

t=0  #variable tipo int
v1=int(input("Hola, suma conmigo. Ingrese un número entero:")) #interacion par ingresar numero
t+=v1
print(t) #imprime el numero ingresado
while v1!=0: #si el numero es diferente a 0
    v1=int(input("Ingrese un número entero(0 para terminar):")) #suma del nuemero ingresado #misma variable con interacion para numero y posibilidad de ingresar 0 para romper bucle
    t+=v1
    print(t)
    
v2=input("Ingrese contraseña:") #interacion de contraseña
con="taller" #contrsaeña denominada
while v2!=con: #mientras contraseña ingresada se diferente a contraseña denominada
    print("Contraseña incorrecta.") #impresion
    v2=input("Ingrese contraseña correcta:") #interacion para volver a escribir contraseña

v3=1 #variable tipo int
while v3<=100: #mientras variable sea menor o igual a 1
    v3=int(input("Ingrese números del 1 al 100 para ver si son pares o impares  y cierre el programa con 111:")) #interacion para ingresar numeros o cerrar bucle
    if v3%2==1: #si el numero ingresado es impar
        print("Número impar") #impresion
    else: print("Número par") #si no es par imprimir numero par

v9=float(input("Ingrese un número para ver su tabla de multiplicar:")) #interacion para mostrar una tabla
tb=1 #variable int para conteo del 1 al 10
while tb<=10: #mientras variable sea menor o igual a 10
    print(f"{v9}x{tb}={v9*tb}") #imprime numero x conteo = resultado
    tb+=1 #suma de 1 en 1 hasta 10

v=1  #variable int para bucle
v10=13 #nuemro para adivinar
print("Hola usuario, adivina el número secreto.Te diré si es mayor o menor en el proceso.") #mensaje para usuario
v11=float(input("Ingresa el número:")) #interacion para ingresar el numero
while v==1: #mientras 1==1 (condicion cierta)
    if v11<v10: #si el numero ingresado es menor al numero secreto
        print("Mayor")
        v11=float(input("Intentalo nuevamente:")) #interacion para intento
    if v11>v10: #si el numero ingresado es mayor al numero secreto
        print("Menor")
        v11=float(input("Intentalo nuevamente:")) #interacion para intento
    if v11==v10: #si el numero ingresado es igual al numero secreto
        print("El número ingresado es correcto.")
        print("¡Felicidades!")
        break #rompe el bucle si llega al numero correcto
    

v12=float(input("Ingrese la tabla de multiplicar que desea tener:")) #interacion para ingresar el numero
for v13 in range(1,11): #iteracion para multiplicar el numero ingresado del 1 al 10
    print(f"{v12}x{v13}={v12*v13}") #imprime numero x conteo = resultado

v13=input("Ingrese una palabra para ver sus letras:") #interacion para ingresar palabra
for v13 in v13: #itere palabra ingresada
    print(v13) #impresion de cada letra
