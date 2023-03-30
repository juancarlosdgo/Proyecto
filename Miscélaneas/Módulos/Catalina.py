import random
Lista=[]
diccionario={}
def llenar_lista(Lista):  #Esta función sirve para llenar una lista con eklementos aletaorios
    for i in range(número):
        Lista.append(random.randint(1,100))
    return Lista
número=int(input("De cuántos números desea la lista: "))
llenar_lista(Lista)
def suma_elementos(Lista): #Esta función sirve para sumar todos los elementos de una lista
    suma=0
    for elemento in Lista:
        suma+=elemento
    return "La suma de los elementos de la lista es:",suma
suma_elementos(Lista)
def conteo(): #Esta función sirve para contar
    cont=0
    while True:
        número=int(input("Ingrese un número, ingrese 0 para finalizar: "))
        if número<=0:
            break
        cont+=1
    return "El usuario ingresó",cont,"números."
def porcentaje():
    valor=int(input("Ingrese el valor: "))    
    porcentaje=int(input("Ingrese el porcentaje: "))
    descuento=valor*(porcentaje/100)
    valor_desc=valor-descuento
    return "El valor con descuento es",valor_desc
def primo():
    n=int(input("Ingrese un número para evaluar si es primo: "))
    cont=0
    for i in range(1,n+1):
        if n%i==0:
            cont+=1
    if cont<=2:
        return n,"Es primo"
    else:
        return n,"No es primo"
