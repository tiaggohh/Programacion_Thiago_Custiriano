# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_10: Crear una función que reciba un numero y retorne 
# True si es primo, False en caso contrario.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

n = int(input("Ingrese un nu" \
"mero: "))
print("¿Es primo?", es_primo(n))
