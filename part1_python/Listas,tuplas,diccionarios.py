#LISTAS----------------------------------------------------------------------------------------

l=[1,2,3,4,5] #lista de numeros
print("Esto es una lista", l)
for i in l: #ciclo for para recorrer la lista
    print(i) #imprime los valores de la lista

l1=[]#lista vacia para almacenar
n=input("Ingresa tu nombre: ") #interacion para nombre
while n!="": #mientras nombre no se valido
    v=input(f"Añade un producto al carrito {n}: ").lower()  #interacion para valor
    l1.append(v) #añade el producto a la lista
    v1=input(f"Deseas terminar la lista {n}? (si/no): ").lower() #interacion para terminar la lista
    if v1=="si": #si la respuesta es si
        print("Tu carrito tiene:", l1)
        print("Adios ",n)
        break #rompe el ciclo
    v2=input(f"Deseas eliminar un producto del carrito {n}? (si/no): ").lower() #interacion para eliminar producto
    if v2=="si": #si la respuesta es si
        v3=input(f"Ingresa el producto a eliminar: {n}") #interacion para producto a eliminar
        if v3 in l1: #si el producto esta en la lista
            l1.remove(v3) #elimina el producto de la lista
            print("Tu carrito tiene:", l1) #imprime la lista actualizada
        else: #si el producto no esta en la lista
            print(f"El producto {v3} no esta en el carrito {n}") #imprime mensaje de error
        break

#TUPLAS--------------------------------------------------------------------------------------

l2=(1,2,3,4,5) #tupla de numeros
print("Esto es una tupla", l2)

for l2 in l2: #ciclo for para recorrer la tupla
    print(l2) #imprime los valores de la tupla
    
v4=input("Deseas crear una tupla? (si/no) ").lower() #interacion para crear tupla
if v4=="si": #si la respuesta es si
    l3=[] #lista vacia para almacenar
    while v4!="": #mientras la respuesta no sea vacia
        v5=float(input(f"Ingresa un número {n}: ")) #interacion para valor
        l3.append(v5) #añade el valor a la lista
        v6=input(f"Deseas terminar la tupla {n}? (si/no)" ).lower() #interacion para terminar la tupla
        if v6=="si": #si la respuesta es si
            t=tuple(l3) #convierte la lista en tupla
            print(f"Tu tupla es: {t}") #imprime la tupla
            print(f"Adios {n}")
            break #rompe el ciclo

#DICCIONARIOS---------------------------------------------------------------------------------

d={"nombre":"Juan","edad":30,"ciudad":"Madrid"} #diccionario con datos
print("Esto es un diccionario", d) #imprime el diccionario

for k,v in d.items(): # itera clave y valor in items del diccionario
    print(k,v) #imprime clave y valor

v7=input(f"Deseas crear un diccionario {n}? (si/no): ").lower() #interacion para crear diccionario
if v7=="si": #si la respuesta es si
    d1={} #diccionario vacio 
    while v7!="": #mientras la respuesta no sea vacia
        k=input(f"Ingresa una clave para el diccionario {n}: ") #interacion para clave
        v=input(f"Ingresa un valor para el diccionario {n}: ") #interacion para valor
        d1[k]=v #añade la clave y valor al diccionario
        v8=input(f"Deseas terminar el diccionario {n}? (si/no): ").lower() #interacion para terminar el diccionario
        if v8=="si": #si la respuesta es si
            print("Tu diccionario es:", d1) #imprime el diccionario
            print("Adios ",n)
            break #rompe el ciclo

