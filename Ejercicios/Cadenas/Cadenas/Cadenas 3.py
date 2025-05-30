# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_2: Crear una función que le solicite al usuario el 
# ingreso de un numero flotante y lo retorne.

def pedir_flotante():
    numero = float(input("Ingrese un numero con decimales: "))
    return numero

n = pedir_flotante()
print("Numero ingresado:", n)
