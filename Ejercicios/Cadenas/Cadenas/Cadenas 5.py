# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_4: Escribir una función que calcule el area de un 
# rectangulo. La función recibe la base y la altura y retorna el area.

def calcular_area_rectangulo(base, altura):
    return base * altura

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
area = calcular_area_rectangulo(base, altura)
print("El area del rectangulo es:", area)
