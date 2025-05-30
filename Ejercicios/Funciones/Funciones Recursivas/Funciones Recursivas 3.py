# Nombre y apellido: Thiago Custiriano
# Div: 211
# Funciones_Recursivas_3:Realizar una función recursiva que permita realizar la
#  suma de los dígitos de un número

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número: "))
print("La suma de los dígitos es:", suma_digitos(numero))
