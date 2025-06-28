# Nombre y apellido: Thiago Custiriano
# Div: 211
# Ordenamiento_1: Función que ordena un array con el método de la burbuja. 
# Puede ser ascendente o descendente.

def ordenar_array(array, descendente=False):
    n = len(array)
    for i in range(n):
        for j in range(n - 1 - i):
            if (not descendente and array[j] > array[j+1]) or (descendente and array[j] < array[j+1]):
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux
    return array

# Prueba
numeros = [5, 2, 8, -3, 0]
print("Ascendente:", ordenar_array(numeros.copy()))
print("Descendente:", ordenar_array(numeros.copy(), True))
