# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_7: Crear una función que verifique si un número dado 
# es par o impar. La función retorna True si es par, False si es impar.

def es_par(numero):
    return numero % 2 == 0

num = int(input("Ingrese un número: "))
resultado = es_par(num)
print("¿Es par?", resultado)
