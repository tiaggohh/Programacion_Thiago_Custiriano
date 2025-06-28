# Nombre y apellido: Thiago Custiriano
# Div: 211
# Arrays_Unidimensionales_10: Mostrar la unión de dos arrays.

def union_arrays(arr1, arr2):
    union = arr1.copy()
    for i in arr2:
        if i not in union:
            union.append(i)
    print("Unión:", union)
