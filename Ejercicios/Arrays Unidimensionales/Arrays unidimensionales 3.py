# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Unidimensionales_3:Escribir una función que reciba una lista de 
# enteros y calcule el promedio de todos los números.

def promedio_lista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)
