# Nombre y apellido: Thiago Custiriano
# Div: 211
# Funciones_Recursivas_4: Realizar una función para calcular el número 
# de Fibonacci de un número ingresado por consola

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

numero = int(input("Ingrese un número: "))
print("El número de Fibonacci es:", fibonacci(numero))
