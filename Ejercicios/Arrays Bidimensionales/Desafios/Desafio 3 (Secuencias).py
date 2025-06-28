# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Bidimensionales_Desafío_3: Detección de Secuencias de Numeros Pares

def ingresar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            num = int(input(f"Ingrese numero en posición [{i}][{j}]: "))
            fila.append(num)
        matriz.append(fila)
    return matriz

def encontrar_secuencias_pares(fila):
    secuencias = []
    secuencia = []
    for num in fila:
        if num % 2 == 0:
            secuencia.append(num)
        else:
            if len(secuencia) >= 2:
                secuencias.append(secuencia)
            secuencia = []
    if len(secuencia) >= 2:
        secuencias.append(secuencia)
    return secuencias

def analizar_matriz(matriz):
    todas = []
    for fila in matriz:
        sec = encontrar_secuencias_pares(fila)
        todas += sec
    return todas

# Programa principal
filas = int(input("Ingrese cantidad de filas: "))
columnas = int(input("Ingrese cantidad de columnas: "))
matriz = ingresar_matriz(filas, columnas)

secuencias = analizar_matriz(matriz)

if len(secuencias) > 0:
    print("✅ EXISTEN NUMEROS CONSECUTIVOS PARES")
    print("Cantidad de secuencias:", len(secuencias))
    
    # Mas corta
    mas_corta = min(secuencias, key=len)
    print("Secuencia mas corta:", mas_corta, "- Largo:", len(mas_corta))
    
    # Mas larga
    mas_larga = max(secuencias, key=len)
    print("Secuencia mas larga:", mas_larga, "- Largo:", len(mas_larga))
else:
    print("❌ NO EXISTEN NUMEROS CONSECUTIVOS PARES")
