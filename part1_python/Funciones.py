#FUNCIONES-----------------------------


n=input("Ingrese su nombre: ")
a=input("Ingrese su apellido: ")

def nombre_completo(n, a):
    return f"{n} {a}"

def saludar(n, a):
    nom_comp= nombre_completo(n, a)
    return f"Ñeldaaa. {nom_comp} que me contas vé!"

def insultar(a,n):
    return f"Vea {n,a} vaya y coma un kilo de monda, eche! ¡Maneje la seriedad!"

def alagar(a, n):
    return f"{n,a} Usted es la monda. Tes@, seguí así"

def despedirse(a, n):
    return f"Hasta luego mi amor, {n,a} mi patacón favorito."

opc=int(input(f"Ingrese la opción que desea realizar: \n 1. Saludar \n 2. Insultar \n 3. Alagar \n 4. Despedirse \n "))

if opc==1:
    print(saludar(n, a))
elif opc==2:
    print(insultar(a, n))
elif opc==3:
    print(alagar(a, n))
elif opc==4:
    print(despedirse(a, n))
else: print("Opción incorrecta. Lea bien.")
