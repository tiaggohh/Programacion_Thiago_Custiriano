# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Cadenas_3: Crear una funcion que reciba como parametro una cadena y
determine si la misma es o no un palindromo Debera retornar un valor booleano indicando lo sucedido.

def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    return cadena == cadena[::-1]


print(es_palindromo("anita lava la tina"))  # True
print(es_palindromo("hola"))  # False
