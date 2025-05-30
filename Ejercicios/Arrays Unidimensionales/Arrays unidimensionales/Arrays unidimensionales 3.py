# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_3: Crear una función que le solicite al usuario el 
# ingreso de una cadena y la retorne.

def pedir_cadena():
    texto = input("Ingrese una cadena de texto: ")
    return texto

cadena = pedir_cadena()
print("Texto ingresado:", cadena)
