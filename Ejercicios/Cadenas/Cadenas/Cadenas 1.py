# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Cadenas_1: Crear una funcion que reciba como parametro una cadena y 
determine la cantidad de vocales que hay de cada una individualmente.

def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    resultado = []

    for vocal in vocales:
        cantidad = cadena.count(vocal)
        resultado.append([vocal, cantidad])
    
    return resultado

print(contar_vocales("murcielaguito"))
