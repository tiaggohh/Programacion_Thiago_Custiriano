# Nombre y apellido: Thiago Custiriano
# Div: 211
# Cadenas_2: Buscar el índice de la primera aparición de un carácter en una cadena.

def primer_indice(cadena, caracter):
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
    return -1


print(primer_indice("murcielaguito", "a"))  # Devuelve 7
