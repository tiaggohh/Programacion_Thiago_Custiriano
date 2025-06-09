# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_1: Implementar una funcion que verifique si una cadena representa
# un numero entero valido positivo o negativo.

def es_entero(cadena):
    if cadena == "":
        return False

    for i in range(len(cadena)):
        c = cadena[i]
        if i == 0 and (c == '+' or c == '-'):
            continue
        if not (ord(c) >= 48 and ord(c) <= 57):
            return False
    return True


print(es_entero("-123"))  # True
print(es_entero("12a3"))  # False
