# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_1: Escribir una funcion que determine
#  si una cadena representa un numero decimal valido con un solo punto decimal.

def es_decimal(cadena):
    if cadena == "":
        return False

    punto = 0
    for i in range(len(cadena)):
        c = cadena[i]
        if i == 0 and (c == '+' or c == '-'):
            continue
        if c == '.':
            punto += 1
            if punto > 1:
                return False
        elif not (ord(c) >= 48 and ord(c) <= 57):
            return False
    return punto == 1


print(es_decimal("-12.34"))  # True
print(es_decimal("12.3.4"))  # False
