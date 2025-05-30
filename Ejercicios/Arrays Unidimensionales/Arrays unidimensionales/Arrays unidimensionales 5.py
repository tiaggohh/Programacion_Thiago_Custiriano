# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_5: Escribir una función que calcule el área de un 
# círculo. La función debe recibir el radio como parámetro y devolver el área.

def calcular_area_circulo(radio):
    return 3.14 * radio * radio

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
print("El área del círculo es:", area)
