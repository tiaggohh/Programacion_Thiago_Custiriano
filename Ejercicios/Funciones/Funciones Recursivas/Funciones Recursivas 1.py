# Nombre y apellido: Thiago Custiriano
# Div: 211
# Funciones_Recursivas_1: Realizar una función recursiva que calcule 
# la suma de los primeros números naturales

def suma_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_naturales(n - 1)

numero = int(input("Ingrese un número: "))
print("La suma es:", suma_naturales(numero))
