# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_4: Escribir una función que calcule el área de un 
# rectángulo. La función recibe la base y la altura y retorna el área.

def calcular_area_rectangulo(base, altura):
    return base * altura

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
area = calcular_area_rectangulo(base, altura)
print("El área del rectángulo es:", area)
