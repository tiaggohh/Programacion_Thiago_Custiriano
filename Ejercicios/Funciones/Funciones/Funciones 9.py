# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_9: Diseñar una función que calcule la potencia de un número. 
# La función debe recibir la base y el exponente y devolver el resultado.

def calcular_potencia(base, exponente):
    return base ** exponente

b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))
resultado = calcular_potencia(b, e)
print("Resultado:", resultado)
