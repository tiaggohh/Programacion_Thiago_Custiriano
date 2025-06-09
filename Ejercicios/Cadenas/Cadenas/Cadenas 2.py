# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Cadenas_2: Crear una funcion que reciba una cadena y un caracter 
La funcion debera devolver el indice en el que se encuentre la primera ocurrencia de dicho caracter o -1 en caso de que no este.

def encontrar_indice(cadena, caracter):
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i
    return -1


print(encontrar_indice("murcielago", "e"))  # 5
print(encontrar_indice("murcielago", "z"))  # -1
