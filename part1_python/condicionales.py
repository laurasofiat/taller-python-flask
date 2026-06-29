# #CONDICIONALES--------------------------------------------

# nom_usuario=input("Ingrese nombre de ususario:") #interacion para nombre

# x=input("¿Tu edad es menor a 18?:") #interacion para respuesta
# if x=="si": #si edad es menor a 18
#     print(nom_usuario,"No cumple con los requisitos.") #imprime
#     print("Puede hacer procesos de crédito.")
# else: print(nom_usuario,"Sí cumple con los requisitos.")
            
# edad=int(input("Ingrese su edad:")) #interacion para edad
# if edad>=1 and edad<=4: #si edad esta entre 1 y 4
#     print("Entrada gratis.")
# elif edad>=5 and edad<9: #si edad esta entre 5 y 9
#     print("Debe pagar 5 euros.") 
# elif edad>=10 and edad<=13: #si edad esta entre 10 y 13
#     print("Debe pagar 10 euros.")
# else: print("Debe pagar 18 euros.") #si

print("Ingrese operación deseada: \n Suma=S----- \n Resta=R----- \n Multiplicación=M----- \n División=D") #impresion de opciones

v=(input("¿qué operación desea realizar?:")).upper() #interaciion para letra- upper para respuesta en mayuscula
v1=float(input("Ingrese un número:")) #numero 1
v2=float(input("Ingrese un número:")) #numero 2
if v=="S": #si es suma
    print("El resultado de la suma es:",v1+v2)
elif v=="R": #si es resta
    print("El resultado de la resta es:",v1-v2)
elif v=="M": #si es multiplicacion
    print("El resultado de la multiplicación es es:",v1*v2)
elif v=="D": #ai es division
    print("El resultado de la división es:",v1/v2)
else: print("Letra incorrecta. Programa cerrado")

