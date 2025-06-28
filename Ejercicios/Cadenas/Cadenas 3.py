# Nombre y apellido: Thiago Custiriano
# Div: 211
# Cadenas_3: Verificar si una cadena es un palíndromo.

def es_palindromo(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    invertida = ""
    for i in range(len(cadena)-1, -1, -1):
        invertida += cadena[i]
    return cadena == invertida


print(es_palindromo("Anita lava la tina"))  # True
