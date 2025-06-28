# Nombre y apellido: Thiago Custiriano
# Div: 211
# Funciones_Recursivas_2: Realizar una función recursiva que calcule la
#  potencia de un número

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print("El resultado es:", potencia(base, exponente))
