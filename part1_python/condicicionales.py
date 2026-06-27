#CONDICIONALES--------------------------------------------

nom_usuario=input("Ingrese nombre de ususario:")
x=input("¿Tu edad es menor a 18?:")
if x=="si":
    print(nom_usuario,"No cumple con los requisitos.")
    print("Puede hacer procesos de crédito.")
else: print(nom_usuario,"Sí cumple con los requisitos.")


edad=int(input("Ingrese su edad:"))
if edad>=1 and edad<=4:
    print("Entrada gratis.")
elif edad>=5 and edad<9:
    print("Debe pagar 5 euros.")
elif edad>=10 and edad<=13:
    print("Debe pagar 10 euros.")

print("Ingrese operación deseada:"
"Suma=S--------------------Resta=R----------------"
"Multiplicación=M----------División=D")
v=(input("¿qué operación desea realizar?:")).upper
v1=float(input("Ingrese un número:"))
v2=float(input("Ingrese un número:"))
if v=="S":
    print("El resultado de la suma es:",v1+v2)
elif v=="R":
    print("El resultado de la resta es:",v1-v2)
elif v=="M":
    print("El resultado de la multiplicación es es:",v1*v2)
elif v=="D":
    print("El resultado de la división es:",v1/v2)