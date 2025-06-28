# Nombre y apellido: Thiago Custiriano
# Div: 211
# Cadenas_1: Contar cuántas veces aparece cada vocal en una cadena.

def contar_vocales(cadena):
    cadena = cadena.lower()
    matriz = [["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0]]

    for letra in cadena:
        for fila in matriz:
            if letra == fila[0]:
                fila[1] += 1
    return matriz


resultado = contar_vocales("murcielaguito")
for vocal in resultado:
    print(f'"{vocal[0]}": {vocal[1]}')
