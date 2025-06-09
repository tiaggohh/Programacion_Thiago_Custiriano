# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Cadenas_5: Crear una funcion que reciba una 
#cadena por parametro y suprima las vocales de la misma.

def eliminar_vocales(cadena):
    resultado = ""
    for letra in cadena:
        if letra.lower() not in "aeiou":
            resultado += letra
    return resultado


print(eliminar_vocales("Hola"))  # Hl
