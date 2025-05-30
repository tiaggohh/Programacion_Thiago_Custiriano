# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Unidimensionales_Desafío_2:
# Menú de Opciones con Listas y Funciones

def ingresar_datos():
    lista = []
    while len(lista) < 10:
        num = int(input("Ingrese un número entre -1000 y 1000: "))
        if -1000 <= num <= 1000:
            lista.append(num)
        else:
            print("Número fuera de rango.")
    return lista

def contar_positivos_negativos(lista):
    positivos = 0
    negativos = 0
    for num in lista:
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
    print("Positivos:", positivos, "| Negativos:", negativos)

def suma_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    print("Suma de pares:", suma)

def mayor_impar(lista):
    mayor = None
    for num in lista:
        if num % 2 != 0:
            if mayor is None or num > mayor:
                mayor = num
    if mayor is not None:
        print("Mayor impar:", mayor)
    else:
        print("No hay impares.")

def listar(lista):
    print("Números ingresados:", lista)

def listar_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    print("Números pares:", pares)

def posiciones_impares(lista):
    impares = []
    for i in range(len(lista)):
        if i % 2 != 0:
            impares.append(lista[i])
    print("Elementos en posiciones impares:", impares)

# Programa principal
numeros = []
while True:
    print("\n--- Menú ---")
    print("1. Ingresar datos")
    print("2. Contar positivos y negativos")
    print("3. Suma de números pares")
    print("4. Mayor número impar")
    print("5. Listar números")
    print("6. Listar pares")
    print("7. Listar posiciones impares")
    print("8. Salir")

    opcion = int(input("Elegí una opción: "))

    if opcion == 1:
        numeros = ingresar_datos()
    elif opcion in [2, 3, 4, 5, 6, 7] and len(numeros) == 0:
        print("Primero tenés que ingresar los datos con la opción 1.")
    elif opcion == 2:
        contar_positivos_negativos(numeros)
    elif opcion == 3:
        suma_pares(numeros)
    elif opcion == 4:
        mayor_impar(numeros)
    elif opcion == 5:
        listar(numeros)
    elif opcion == 6:
        listar_pares(numeros)
    elif opcion == 7:
        posiciones_impares(numeros)
    elif opcion == 8:
        print("Chau, saliste del programa.")
        break
    else:
        print("Opción inválida.")
