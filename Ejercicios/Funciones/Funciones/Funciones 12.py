# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_12: Crear una función que imprima la tabla de multiplicar 
# de un numero. Puede tener parámetros opcionales para inicio y fin (por defecto 1 a 10).

def tabla_multiplicar(numero, inicio=1, fin=10):
    for i in range(inicio, fin + 1):
        print(f"{numero} x {i} = {numero * i}")

n = int(input("Ingrese un numero: "))
tabla_multiplicar(n)
