# Nombre y apellido: Thiago Custiriano
# Div: 211
# Cadenas_4: Eliminar caracteres repetidos consecutivos.

def eliminar_repetidos(cadena):
    nueva = ""
    for i in range(len(cadena)):
        if i == 0 or cadena[i] != cadena[i - 1]:
            nueva += cadena[i]
    return nueva

#prueba
print(eliminar_repetidos("Hooola"))  # "Hola"
