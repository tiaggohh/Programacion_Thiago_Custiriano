# Nombre y apellido: Thiago Custiriano
# Div: 211
# Cadenas_5: Eliminar todas las vocales de una cadena.

def eliminar_vocales(cadena):
    resultado = ""
    for letra in cadena:
        if letra.lower() not in "aeiou":
            resultado += letra
    return resultado

#prueba
print(eliminar_vocales("Hola"))  # "Hl"
