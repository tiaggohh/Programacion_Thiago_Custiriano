# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Unidimensionales_4: Calcular y devolver el promedio de los números positivos.

def promedio_positivos(lista):
    suma = 0
    contador = 0
    for i in lista:
        if i > 0:
            suma += i
            contador += 1
    if contador > 0:
        return suma / contador
    else:
        return 0
