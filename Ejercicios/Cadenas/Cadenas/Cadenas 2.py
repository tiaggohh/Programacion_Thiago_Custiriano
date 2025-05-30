# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_1: Crear una función que le solicite al usuario el 
# ingreso de un numero entero y lo retorne.

def pedir_entero():
    numero = int(input("Ingrese un numero entero: "))
    return numero

n = pedir_entero()
print("Numero ingresado:", n)
