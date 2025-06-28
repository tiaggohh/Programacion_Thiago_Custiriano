# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Bidimensionales_Desafio_3:
# Gestion de Recaudaciones en Empresa de Colectivos

import random

def generar_legajos():
    legajos = []
    while len(legajos) < 15:
        legajo = random.randint(1000, 9999)
        if legajo not in legajos:
            legajos.append(legajo)
    return legajos

def mostrar_recaudaciones(recaudaciones):
    for i in range(3):
        print(f"Linea {i+1}: {recaudaciones[i]}")

def cargar_recaudacion(legajos, recaudaciones):
    legajo = int(input("Ingrese su número de legajo: "))
    if legajo in legajos:
        linea = int(input("Linea (1 a 3): ")) - 1
        coche = int(input("Coche (1 a 5): ")) - 1
        if 0 <= linea < 3 and 0 <= coche < 5:
            monto = int(input("Monto recaudado: "))
            if monto >= 0:
                recaudaciones[linea][coche] += monto
                print("✅ Recaudacion registrada.")
            else:
                print("❌ Monto invalido.")
        else:
            print("❌ Linea o coche invalido.")
    else:
        print("❌ Legajo no encontrado.")

# Programa principal
legajos = generar_legajos()
recaudaciones = [[0] * 5 for _ in range(3)]

while True:
    print("\n--- Menú ---")
    print("1. Cargar recaudacion")
    print("2. Ver recaudacion por coche y linea")
    print("3. Ver recaudacion por linea")
    print("4. Ver recaudacion por coche")
    print("5. Ver recaudacion total")
    print("6. Salir")
    opcion = int(input("opcion: "))

    if opcion == 1:
        cargar_recaudacion(legajos, recaudaciones)
    elif opcion == 2:
        mostrar_recaudaciones(recaudaciones)
    elif opcion == 3:
        for i in range(3):
            print(f"Linea {i+1} total: {sum(recaudaciones[i])}")
    elif opcion == 4:
        coche = int(input("Ingrese número de coche (1 a 5): ")) - 1
        if 0 <= coche < 5:
            total = 0
            for i in range(3):
                total += recaudaciones[i][coche]
            print(f"Total del coche {coche+1}: {total}")
        else:
            print("❌ Coche invalido.")
    elif opcion == 5:
        total = 0
        for fila in recaudaciones:
            total += sum(fila)
        print("Total general recaudado:", total)
    elif opcion == 6:
        print("Chau, saliste del programa.")
        break
    else:
        print("❌ opcion invalida.")
