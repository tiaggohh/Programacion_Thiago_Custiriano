# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Bidimensionales_Desafío_2: Verificación de un Cuadrado Magico

def ingresar_cuadrado(n):
    matriz = []
    usados = []
    for i in range(n):
        fila = []
        for j in range(n):
            while True:
                num = int(input(f"Ingrese número entre 1 y {n*n} en [{i}][{j}]: "))
                if 1 <= num <= n*n and num not in usados:
                    usados.append(num)
                    fila.append(num)
                    break
                else:
                    print("Número invalido o repetido.")
        matriz.append(fila)
    return matriz

def es_cuadrado_magico(matriz):
    n = len(matriz)
    suma_ref = sum(matriz[0])

    # filas
    for fila in matriz:
        if sum(fila) != suma_ref:
            return False

    # columnas
    for j in range(n):
        suma_col = 0
        for i in range(n):
            suma_col += matriz[i][j]
        if suma_col != suma_ref:
            return False

    # diagonal principal
    suma_diag1 = sum(matriz[i][i] for i in range(n))
    if suma_diag1 != suma_ref:
        return False

    # diagonal secundaria
    suma_diag2 = sum(matriz[i][n - 1 - i] for i in range(n))
    if suma_diag2 != suma_ref:
        return False

    return True

# Programa principal
n = int(input("Ingrese el tamaño del cuadrado magico (ej: 3 para 3x3): "))
cuadrado = ingresar_cuadrado(n)

print("\nMatriz ingresada:")
for fila in cuadrado:
    print(fila)

if es_cuadrado_magico(cuadrado):
    print("✅ ES UN CUADRADO MAGICO")
else:
    print("❌ NO ES UN CUADRADO MAGICO")
