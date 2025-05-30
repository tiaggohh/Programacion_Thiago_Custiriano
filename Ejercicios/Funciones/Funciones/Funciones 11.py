# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ejercicio_Funciones_11: Crear una función que muestre todos los numeros 
# primos entre 1 y un numero dado. Retorna la cantidad de primos encontrados.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def mostrar_primos(hasta):
    cantidad = 0
    for i in range(1, hasta + 1):
        if es_primo(i):
            print(i)
            cantidad += 1
    return cantidad

limite = int(input("Ingrese un numero: "))
total = mostrar_primos(limite)
print("Cantidad de numeros primos:", total)
