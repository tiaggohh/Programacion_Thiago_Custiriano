# Nombre y apellido: Thiago Custiriano
# Div: 211
# Desafio_1: Crear una funcion que valide si una contrasena cumple ciertas condiciones de seguridad.

def clave_segura(clave):
    tiene_mayus = False
    tiene_minus = False
    tiene_numero = False
    contador = 0

    for c in clave:
        codigo = ord(c)
        contador += 1
        if codigo >= 65 and codigo <= 90:
            tiene_mayus = True
        elif codigo >= 97 and codigo <= 122:
            tiene_minus = True
        elif codigo >= 48 and codigo <= 57:
            tiene_numero = True

    return tiene_mayus and tiene_minus and tiene_numero and contador >= 8


print(clave_segura("Abc12345"))  # True
print(clave_segura("abcdef"))  # False
