# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ordenamiento_2:
# Función que intercala dos vectores ordenados y devuelve uno solo también ordenado.

def ordenar_array(array, descendente=False):
    n = len(array)
    for i in range(n):
        for j in range(n - 1 - i):
            if (not descendente and array[j] > array[j+1]) or (descendente and array[j] < array[j+1]):
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux
    return array


def intercalar_vectores(vec1, vec2, descendente=False):
    resultado = []
    i = 0
    j = 0

    while i < len(vec1) and j < len(vec2):
        if vec1[i] < vec2[j]:
            resultado.append(vec1[i])
            i += 1
        else:
            resultado.append(vec2[j])
            j += 1

    while i < len(vec1):
        resultado.append(vec1[i])
        i += 1

    while j < len(vec2):
        resultado.append(vec2[j])
        j += 1

    if descendente:
        resultado = ordenar_array(resultado, True)  # usando la función del ejercicio 1
    return resultado

# Prueba
v1 = [1, 3, 5]
v2 = [2, 4, 6]
print("Intercalado ascendente:", intercalar_vectores(v1, v2))
print("Intercalado descendente:", intercalar_vectores(v1, v2, True))
