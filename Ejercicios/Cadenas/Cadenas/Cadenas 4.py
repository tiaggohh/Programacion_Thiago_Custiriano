# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Cadenas_4: Crear una funcion que reciba como parametro 
una cadena y suprima los caracteres repetidos consecutivos.

def suprimir_repetidos_consecutivos(cadena):
    if cadena == "":
        return ""

    resultado = cadena[0]

    for i in range(1, len(cadena)):
        if cadena[i] != cadena[i - 1]:
            resultado += cadena[i]

    return resultado


print(suprimir_repetidos_consecutivos("Hooola"))  # Hola
