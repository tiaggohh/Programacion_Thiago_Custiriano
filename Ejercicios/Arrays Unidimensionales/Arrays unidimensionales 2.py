# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Unidimensionales_2: Escribir una función que permita ingresar la cantidad de 
# números que reciba como parámetro. Crear el array con la función del punto 1.

def cargar_array(cantidad):
    lista = []
    for i in range(cantidad):
        numero = int(input("Ingrese un número: "))
        lista.append(numero)
    return lista
