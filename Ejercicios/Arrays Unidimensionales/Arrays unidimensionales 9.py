# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Unidimensionales_9:Mostrar la intersección entre dos arrays.

def interseccion_arrays(arr1, arr2):
    for i in arr1:
        if i in arr2:
            print("Elemento en común:", i)
