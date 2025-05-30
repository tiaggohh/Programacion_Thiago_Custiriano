# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_8: Definir una función que encuentre el máximo de tres 
# números. La función debe aceptar tres argumentos y devolver el mayor.

def maximo_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
z = int(input("Ingrese el tercer número: "))
mayor = maximo_de_tres(x, y, z)
print("El número mayor es:", mayor)
